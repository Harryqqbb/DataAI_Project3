import numpy as np
import pandas as pd

# Load data
df = pd.read_csv("SiHits_3D_pvar_zvar_0.03_0.00_28_0.04_0.06_100_v1.txt", header=None)
df.columns = ["frame_id", "true_z", "track_id", "point_id", "dx", "dy", "dz", "x", "y", "z"]

# Group by each unique frame
frame_errors = []
frame_results = []

for frame_id, group in df.groupby("frame_id"):
    true_z = group["true_z"].iloc[0]
    directions = group[["dx", "dy", "dz"]].to_numpy()
    points = group[["x", "y", "z"]].to_numpy()

    # Normalize direction vectors
    norms = np.linalg.norm(directions, axis=1).reshape(-1, 1)
    directions = directions / norms

    # Solve using least squares
    A = np.zeros((3, 3))
    b = np.zeros(3)

    for d, p in zip(directions, points):
        d = d.reshape(3, 1)
        P = np.eye(3) - d @ d.T
        A += P
        b += P @ p

    try:
        vertex = np.linalg.solve(A, b)
        estimated_z = vertex[2]
        error = abs(estimated_z - true_z)

        frame_errors.append(error)
        frame_results.append((frame_id, true_z, estimated_z, error))
    except np.linalg.LinAlgError:
        print(f"Frame {frame_id}: Skipped (singular matrix)")
        continue

# Convert to DataFrame for stats
results_df = pd.DataFrame(frame_results, columns=["frame_id", "true_z", "estimated_z", "z_error"])

# Print all results
print("\nPer-frame Z error:")
print(results_df.to_string(index=False))

# Summary statistics
mean_error = results_df["z_error"].mean()
std_dev = results_df["z_error"].std()
min_error = results_df["z_error"].min()
max_error = results_df["z_error"].max()

print("\nSummary statistics:")
print(f"Total frames processed: {len(results_df)}")
print(f"Mean Z error:          {mean_error:.6f}")
print(f"Standard deviation:    {std_dev:.6f}")
print(f"Minimum Z error:       {min_error:.6f}")
print(f"Maximum Z error:       {max_error:.6f}")
