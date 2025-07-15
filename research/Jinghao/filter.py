import numpy as np
import pandas as pd

## Generates file with filtered data, everything below -6 is deleted
input_file = 'SiHits_3D_pvar_0.02_0.50_100_v0.txt'
output_file = 'filtered_above_z.txt'
z_col_index = 8                                      # Z axis is the 9th column (index 8)

data = np.loadtxt(input_file, delimiter=',')

# === Filter out rows where Z < -6 ===
filtered_data = data[data[:, z_col_index] >= -6]

np.savetxt(output_file, filtered_data, delimiter=',', fmt='%.4f')

## Generates a file based off of distance from detector
df = pd.read_csv("first_frame.txt", header=None)
df.columns = ['frame_id', 'track_id', 'point_id', 'dx', 'dy', 'dz', 'x', 'y', 'z']

df['radial_xy'] = np.sqrt(df['x']**2 + df['y']**2)

filtered = df[(df['radial_xy'] > 0.5)]

# Sort from greatest to least radial XY distance
filtered_sorted = filtered.sort_values(by='radial_xy', ascending=False)

# Save to CSV
output_file = "filtered_xy_sorted.csv"
filtered_sorted.to_csv(output_file, index=False)