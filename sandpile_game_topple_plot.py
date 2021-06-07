import numpy as np
import matplotlib.pyplot as plt

import finite_sandpiles as fsp


a = np.zeros((16, 16))
b = np.zeros((6, 6, 6))
c = np.zeros((4, 4, 4, 4))

xs = []
ys_a = []
ys_b = []
ys_c = []

for iter in range(1000):
    fsp.add_random(a)
    fsp.add_random(b)
    fsp.add_random(c)
    xs.append(iter)
    ys_a.append(fsp.topple(a))
    ys_b.append(fsp.topple(b))
    ys_c.append(fsp.topple(c))
    # plt.matshow(a, vmin=0, vmax=3)
    # plt.show()

plt.plot(xs, ys_a, label="2d")
plt.plot(xs, ys_b, label="3d")
plt.plot(xs, ys_c, label="4d")
plt.legend()
plt.show()
