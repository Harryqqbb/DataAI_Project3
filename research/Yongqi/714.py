# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   # noqa: F401  仅注册 3D

# 1. 读数据
pts = np.loadtxt('/Users/biming/Desktop/3/SiHits_3D_pvar_0.02_0.50_100_v0.txt',delimiter=",")            # shape = (N, 3)
x, y, z = pts[:,6], pts[:,7], pts[:,8]
# 2. 画大图
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=z, cmap='viridis', s=8)   # 颜色按 z 值渐变
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
plt.tight_layout()
plt.show()

pts   = np.loadtxt('/Users/biming/Desktop/3/SiHits_3D_pvar_0.02_0.50_100_v0.txt', delimiter=',')
x, y, z, grp = pts[:, 6], pts[:, 7], pts[:, 8], pts[:, 0].astype(int)
# 2) 每个 group 单独子图
groups = np.unique(grp)
cols   = int(np.ceil(np.sqrt(len(groups))))
rows   = int(np.ceil(len(groups) / cols))
fig = plt.figure(figsize=(cols*4, rows*3))
for i, g in enumerate(groups, 1):
    mask = grp == g
    ax = fig.add_subplot(rows, cols, i, projection='3d')
    ax.scatter(x[mask], y[mask], z[mask], s=8)
    ax.set_title(f'group {g}')
plt.tight_layout(); plt.show()


pts = np.loadtxt('/Users/biming/Desktop/3/filtered_above_z.txt', delimiter=',')
y, z = pts[:, 7], pts[:, 8]
# 绘制 2D 散点图y-z
plt.figure(figsize=(8, 6))
plt.scatter(y, z, s=8)
plt.xlabel('Y')
plt.ylabel('Z')
plt.title('2D Scatter Plot of Y vs Z')
plt.tight_layout()
plt.show()