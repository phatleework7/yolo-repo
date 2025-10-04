import heapq
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def trapRainWater(heightMap):
    if not heightMap or not heightMap[0]:
        return 0

    m, n = len(heightMap), len(heightMap[0])
    visited = [[False]*n for _ in range(m)]
    heap = []

    # Push boundary cells
    for i in range(m):
        for j in [0, n-1]:
            heapq.heappush(heap, (heightMap[i][j], i, j))
            visited[i][j] = True
    for j in range(n):
        for i in [0, m-1]:
            if not visited[i][j]:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True

    water = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    max_height = 0

    while heap:
        h, x, y = heapq.heappop(heap)
        max_height = max(max_height, h)
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                nh = heightMap[nx][ny]
                if nh < max_height:
                    water += max_height - nh
                heapq.heappush(heap, (nh, nx, ny))
    return water

# Ví dụ input
heightMap = [
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

# Tính nước
print("Trapped water:", trapRainWater(heightMap))

# Vẽ mô phỏng 3D
arr = np.array(heightMap)
x, y = np.meshgrid(range(arr.shape[1]), range(arr.shape[0]))

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, arr, cmap="terrain", edgecolor="k")
ax.set_title("3D Elevation Map")
plt.show()
