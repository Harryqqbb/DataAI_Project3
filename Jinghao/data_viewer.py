import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load data
data = np.loadtxt('SiHits_3D_pvar_0.02_0.50_100_v0.txt', delimiter=',')

# Extract x, y, z from columns 6, 7, 8
x = data[:, 6]
y = data[:, 7]
z = data[:, 8]

# Create 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, s=1, alpha=0.6)

# Label axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Scatter Plot of Hits')

plt.tight_layout()
plt.show()
