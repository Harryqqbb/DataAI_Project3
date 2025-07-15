# Re-import necessary packages after environment reset
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Reload the dataset
file_path = "SiHits_3D_pvar_zvar_0.03_0.00_28_0.04_0.06_100_v1.txt"
df = pd.read_csv(file_path, header=None)
df.columns = ["event_id", "true_z", "path_id", "point_id", "nx", "ny", "nz", "x", "y", "z"]

# Group by event only (ignore path_id)
grouped = df.groupby("event_id")

# Prepare storage for results
errors = []
comparison_records = []

# Process each event independently
for event_id, group in grouped:
    true_z = group["true_z"].iloc[0]
    
    # Linear regression in Y-Z plane
    X = group["y"].values.reshape(-1, 1)
    y = group["z"].values

    if len(np.unique(X)) < 2:
        continue  # Skip if there's not enough variation for regression

    model = LinearRegression().fit(X, y)
    predicted_z = model.predict([[0]])[0]
    error = predicted_z - true_z
    errors.append(error)
    comparison_records.append((event_id, true_z, predicted_z, error))

# Convert results to DataFrame for display
results_df = pd.DataFrame(comparison_records, columns=["Event", "True Z", "Predicted Z", "Error"])

# Compute statistics
print(np.mean(errors))
print(np.std(errors))
