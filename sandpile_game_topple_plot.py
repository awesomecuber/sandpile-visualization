import numpy as np
import matplotlib.pyplot as plt

import finite_sandpiles as fsp


a = np.zeros((5, 5, 5))

xs = []
ys = []

for iter in range(0, 1000):
    fsp.add_random(a)
    xs.append(iter)
    ys.append(fsp.topple(a))
    # plt.matshow(a, vmin=0, vmax=3)
    # plt.show()

plt.plot(xs, ys)
plt.show()
