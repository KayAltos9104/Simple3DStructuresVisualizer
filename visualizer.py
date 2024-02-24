import random
import matplotlib.pyplot as plt

x = []
y = []
z = []
x_cut = 0
y_cut = 0
z_cut = 0
coords = []

def create_xyz(lx, ly, lz, x_cut=0, y_cut=0, z_cut=0):
    global x,y,z
    x = []
    y = []
    z = []
    for i in range(0, lx):
        for j in range(0, ly):
            for k in range(0, lz):
                if random.randint(0, 100) <= 100:
                    if i >= x_cut or j >= y_cut or k >= z_cut:
                        x.append(i)
                        y.append(j)
                        z.append(k)


def read_structure(path):
    global coords, x_cut, y_cut, z_cut
    coords = []
    size = None
    with open(path) as f:
        begin = 0
        s = None
        while True:
            s = f.readline()
            begin += 1
            if 'Structure' in s:
                break
            if 'Size' in s:
                row = s.split('=')
                size = row[1].split(';')
                x_cut = int(size[0])
                y_cut = int(size[1])
                z_cut = int(size[2])
        number = 0
        for item in f:
            # print(f'Проверено {number} строк')
            coords.append(item)
            number += 1


def visualize():
    global x_cut, y_cut, z_cut, x, y, z
    x = []
    y = []
    z = []
    for item in coords:
        coord = item.split()
        if int(coord[3]) != 0:
            if int(coord[0]) < x_cut or int(coord[1]) < y_cut or int(coord[2]) < z_cut:
                x.append(int(coord[0]))
                y.append(int(coord[1]))
                z.append(int(coord[2]))
    #create_xyz(50, 50, 50, x_cut=0, y_cut=0, z_cut=0)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(x, y, z, marker='o', s=7, c='#2af7ed', edgecolors='black', depthshade=True)
    #ax.scatter(x, y, z, marker='o', s=8, c='blue', edgecolors='black', depthshade=True)
    plt.axis('off')
    plt.show()



