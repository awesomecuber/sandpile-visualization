import matplotlib.pyplot as plt

piles = [[2, 1, 2],
         [1, 0, 1],
         [2, 1, 2]]

plt.matshow(piles, vmin=0, vmax=4)
plt.show()