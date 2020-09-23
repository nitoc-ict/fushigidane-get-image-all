import numpy as np
import matplotlib.pyplot as plt

count = 0
data = []
for i, j in zip(np.linspace(26.548070, 26.824258, 20), np.linspace(127.981836, 128.250277, 20)):
    for n in np.linspace(0, 0.109069, 50):
        #print(j, i+n, count)
        data.append([i, j+n])
        count += 1

for i in np.linspace(127.876367, 128.037616, 30):
    for j in np.linspace(26.589016, 26.709945, 30):
        data.append([j, i])
        count += 1

for i, j in zip(np.linspace(26.471451, 26.574122, 20), np.linspace(127.832440, 127.982565, 20)):
    for n in np.linspace(0, 0.106271, 50):
        data.append([i, j+n])
        count += 1

for i, j in zip(np.linspace(26.148143, 26.434354, 50), np.linspace(127.618184, 127.717325, 50)):
    for n in np.linspace(0, 0.154768, 150):
        data.append([i, j+n])
        count += 1

print(count)
x, y = zip(*data)
plt.scatter(x, y)
plt.savefig('img.png')
plt.show()