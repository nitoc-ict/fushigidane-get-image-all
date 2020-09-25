import get_image
import numpy as np
#  import matplotlib.pyplot as plt

count = 0
data = []
for i, j in zip(np.linspace(26.575009, 26.824258, 20), np.linspace(127.981836, 128.244362, 20)):
    for n in np.linspace(0, 0.166134, 50):
        data.append([i, j+n])


for j in np.linspace(26.589016, 26.709945, 30):
    for i in np.linspace(127.876367, 128.037616, 30):
        data.append([j, i])

for i, j in zip(np.linspace(26.459480, 26.552919, 20), np.linspace(127.824643, 127.970443, 20)):
    for n in np.linspace(0, 0.109597, 50):
        data.append([i, j+n])

for i, j in zip(np.linspace(26.098296, 26.434354, 50), np.linspace(127.651460, 127.717325, 50)):
    for n in np.linspace(0, 0.154768, 150):
        data.append([i, j+n])


count = 0

#print(data[8258])

#  ここで写真おとす
for count, point in enumerate(data):
    print(count)
    print(point)
    if count >= START_COUNT:
        get_image.get_image(point)
