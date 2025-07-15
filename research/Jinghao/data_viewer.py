import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load data
data = np.loadtxt('first_frame.txt', delimiter=',')

# Extract x, y, z from columns 6, 7, 8
x = data[:, 3]
y = data[:, 4]
z = data[:, 5]

# Create 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the first point in red
ax.scatter(x[0], y[0], z[0], s=1, color='red', label='First Point')

# Plot the rest of the points
ax.scatter(x[1:], y[1:], z[1:], s=1, alpha=0.6)

# Label axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Scatter Plot of Hits')

plt.tight_layout()
plt.show()
