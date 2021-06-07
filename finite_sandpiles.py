import random

import numpy as np
import matplotlib.pyplot as plt

def topple(piles: np.ndarray):
    cutoff = 2 * piles.ndim
    coords_to_topple = np.argwhere(piles >= cutoff).tolist()

    num_topples = 0
    while len(coords_to_topple) > 0:
        topple_coord, coords_to_topple = coords_to_topple[-1], coords_to_topple[:-1]

        topple_times = piles[tuple(topple_coord)] // cutoff
        piles[tuple(topple_coord)] -= cutoff * topple_times

        num_topples += topple_times

        for dimension in range(0, piles.ndim):
            forward_pile = topple_coord.copy()
            forward_pile[dimension] += 1
            backward_pile = topple_coord.copy()
            backward_pile[dimension] -= 1

            if forward_pile[dimension] < piles.shape[dimension]:
                piles[tuple(forward_pile)] += topple_times
                if piles[tuple(forward_pile)] >= cutoff:
                    coords_to_topple.append(forward_pile)

            if backward_pile[dimension] > -1:
                piles[tuple(backward_pile)] += topple_times
                if piles[tuple(backward_pile)] >= cutoff:
                    coords_to_topple.append(backward_pile)
    return num_topples

def add_random(piles: np.ndarray):
    piles_shape = piles.shape
    random_index = [random.randint(0, shape - 1) for shape in piles_shape]
    piles[tuple(random_index)] += 1

if __name__ == "__main__":
    piles = np.zeros((5, 5))
    for _ in range(10000):
        add_random(piles)
        topple(piles)
    plt.matshow(piles, vmin=0, vmax=3)
    plt.show()