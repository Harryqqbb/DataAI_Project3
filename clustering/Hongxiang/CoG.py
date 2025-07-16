import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def compute_local_cog(image, center, window=5):

    y0, x0 = int(round(center[0])), int(round(center[1]))
    half_w = window // 2

    # 截取图像窗口
    x_min = max(x0 - half_w, 0)
    x_max = min(x0 + half_w + 1, image.shape[1])
    y_min = max(y0 - half_w, 0)
    y_max = min(y0 + half_w + 1, image.shape[0])


    sub_img = image[y_min:y_max, x_min:x_max]

    # 构造坐标网格
    xs, ys = np.meshgrid(np.arange(x_min, x_max), np.arange(y_min, y_max))

    total_intensity = np.sum(sub_img)
    if total_intensity == 0:
        return center  # 避免除以0

    cog_x = np.sum(xs * sub_img) / total_intensity
    cog_y = np.sum(ys * sub_img) / total_intensity
    # print("cog_x", cog_x)
    # print("cog_y", cog_y)
    return [cog_x, cog_y]


def read_event_file(filepath, max_events=10):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    num_clusters_lis = []
    cluster_coords = []
    image_lis = []
    x = 0
    event_count = 0

    while x < len(lines) and event_count < max_events:
        num_clusters = int(lines[x].strip())
        num_clusters_lis.append(num_clusters)

        coords = []
        for i in range(x+1, x+1 + num_clusters):
            cx, cy = map(float, lines[i].strip().split())
            coords.append((cx, cy))
        cluster_coords.append(coords)

        # 读取图像像素值
        pixel_values = []
        line_idx = x + 1 + num_clusters
        while len(pixel_values) < 64 * 64:
            pixel_values.extend([float(a) for a in lines[line_idx].strip().split()])
            line_idx += 1

        image = np.array(pixel_values).reshape((64, 64))
        image_lis.append(image)

        x = line_idx  # 移动到下一个事件起点
        event_count += 1

    return num_clusters_lis, np.array(cluster_coords, dtype=object), np.array(image_lis)


num_clusters_lis1,cluster_coords1, image_lis1=read_event_file('../data/Clusters_2D_100_10.txt')



predict_cords=[]
for i in range(num_clusters_lis1[0]):
    coor=compute_local_cog(image_lis1[0], cluster_coords1[0,i])

    predict_cords.append(coor)


predict_cords = np.array(predict_cords)
print(predict_cords)

# np.savetxt('my_array.txt', image_lis1[0], fmt='%.4f')  # 可以调整精度

