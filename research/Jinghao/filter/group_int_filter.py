import pandas as pd
import numpy as np
import os

# === Configuration ===
tolerance = 0.1                  # Acceptable distance from integer center
input_file = 'first_frame.txt'
output_folder = 'clusters'      # Folder to store the cluster files

# === Load data ===
df = pd.read_csv(input_file, header=None)
df.columns = ['frame_id', 'track_id', 'point_id', 'dx', 'dy', 'dz', 'x', 'y', 'z']

# === Compute distance from origin ===
df['distance'] = np.sqrt(df['x']**2 + df['y']**2)

# === Round distance to nearest integer ===
df['rounded_dist'] = np.round(df['distance'])

# === Create output folder if needed ===
os.makedirs(output_folder, exist_ok=True)

# === Identify all unique integer cluster centers within tolerance ===
unique_clusters = sorted(df[np.abs(df['distance'] - df['rounded_dist']) <= tolerance]['rounded_dist'].unique())

# === Save each cluster group to its own CSV ===
total_saved = 0
for center in unique_clusters:
    mask = np.abs(df['distance'] - center) <= tolerance
    cluster_df = df[mask].copy()
    if not cluster_df.empty:
        filename = f"{output_folder}/cluster_{int(center)}.csv"
        cluster_df.to_csv(filename, index=False)
        print(f"✅ Saved cluster {int(center)} with {len(cluster_df)} points → {filename}")
        total_saved += 1