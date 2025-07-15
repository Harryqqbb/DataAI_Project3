import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

f=pd.read_csv('../data/filtered_above_z.txt', delimiter=',',names=['img','n1','n2','n3','n4','n5','x','y','z'])

data=f[['img','x','y','z']]
data['dis'] = np.sqrt(data['x']**2 + data['y']**2)
data = data.sort_values(by='dis', ascending=False)
plt.hist(data['dis'],bins=300)
plt.show()
data.to_csv('filtered_xy_dis_sorted.csv', index=False)

