import pandas as pd
import numpy as np
from collections import defaultdict
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the dataset
file_path = "SiHits_3D_pvar_zvar_0.03_0.00_28_0.04_0.06_100_v1.txt"
df = pd.read_csv(file_path, header=None)
df.columns = ["event_id", "true_z", "path_id", "point_id", "nx", "ny", "nz", "x", "y", "z"]
grouped = df.groupby(["event_id", "path_id"])

# Dictionary to hold predictions per event
event_predictions = defaultdict(list)
event_true_z = {}

# Using Lin. Reg. to guestimate center
for (event_id, path_id), group in grouped:
    z = group["y"].values.reshape(-1, 1)
    y = group["z"].values
    if len(np.unique(z)) < 2:
        continue

    reg = LinearRegression().fit(z, y) 
    z_at_y0 = reg.predict(np.array([[0]]))[0]
    event_predictions[event_id].append(z_at_y0)
    event_true_z[event_id] = group["true_z"].iloc[0]

# Calculate errors and standard deviation per event
errors = []
for event_id, preds in event_predictions.items():
    true_z = event_true_z[event_id]
    for pred_z in preds:
        errors.append(pred_z - true_z)
        
# # Print all comparisons and errors
# for event_id, preds in event_predictions.items():
#     true_z = event_true_z[event_id]
#     for pred_z in preds:
#         error = pred_z - true_z
#         print(f"{event_id:<6} {true_z:>10.4f} {pred_z:>15.4f} {error:>10.4f}")

errors = np.array(errors)
std_dev = np.std(errors)
mean_error = np.mean(errors)

print("Average Error (mean of predicted_z - true_z):", mean_error)
print("Standard Deviation of Errors:", std_dev)

plt.figure(figsize=(10, 6))
plt.hist(errors, bins=50, color='steelblue', edgecolor='black')
plt.title('Histogram of Z Prediction Errors')
plt.xlabel('Prediction Error (predicted_z - true_z)')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()