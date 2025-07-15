import numpy as np

# === Configuration ===
input_file = 'SiHits_3D_pvar_0.02_0.50_100_v0.txt'  # Original data file
output_file = 'filtered_above_z.txt'                # Output file
z_col_index = 8                                      # Z axis is the 9th column (index 8)

# === Load the data ===
data = np.loadtxt(input_file, delimiter=',')

# === Filter out rows where Z < -6 ===
filtered_data = data[data[:, z_col_index] >= -6]

# === Save the result ===
np.savetxt(output_file, filtered_data, delimiter=',', fmt='%.4f')

print(f"Filtered data saved to: {output_file}")
