import numpy as np
import pandas as pd

input_file = 'SiHits_3D_pvar_0.02_0.50_100_v0.txt'
output_file = 'filtered_above_z.txt'
z_col_index = 8 

data = np.loadtxt(input_file, delimiter=',')

filtered_data = data[data[:, z_col_index] >= -6]

np.savetxt(output_file, filtered_data, delimiter=',', fmt='%.4f')