import pandas as pd
import numpy as np

df = pd.read_csv("first_frame.txt", header=None)
df.columns = ['frame_id', 'track_id', 'point_id', 'dx', 'dy', 'dz', 'x', 'y', 'z']

df['radial_xy'] = np.sqrt(df['x']**2 + df['y']**2)

filtered = df[(df['radial_xy'] > 0.5)]

filtered_sorted = filtered.sort_values(by='radial_xy', ascending=False)

# Save to CSV
output_file = "filtered_xy_sorted.csv"
filtered_sorted.to_csv(output_file, index=False)