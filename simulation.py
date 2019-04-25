import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

# right now i've set up the plotting to work with an array (or list i guess) of
# 3D
point = np.array([[[1.0, 1.0, 1.0], [23, 30, 32], [3.0, 30, 34]],
                  [[2.4, 3.0, 2.9], [21, 36, 34], [2.0, 30, 39]]
                  ])


# Sets up plot
fig = plt.figure()
ax = p3.Axes3D(fig)

plt.xscale(0, 100)

for i in [0, 1]:
    print(i)
    ax.scatter(point[i][0], point[i][1], point[i][2])
    plt.savefig("figures/figure" + str(i))
    plt.cla()



import os
print(os.getcwd())

os.path.join("hello", "world")
