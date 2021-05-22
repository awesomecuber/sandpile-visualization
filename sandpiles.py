# infinite size

import math
import timeit

import matplotlib.pyplot as plt
import numpy as np

def topple(piles):
    coords_to_topple: set[tuple[int, int]] = set()
    for pile_coord, pile_size in piles.items():
        if pile_size > 3:
            coords_to_topple.add(pile_coord)

    num_topples = 0
    while len(coords_to_topple) > 0:
        topple_coord = coords_to_topple.pop()

        topple_times = piles[topple_coord] // 4
        piles[topple_coord] -= 4 * topple_times

        num_topples += topple_times

        left_coord = (topple_coord[0] - 1, topple_coord[1])
        right_coord = (topple_coord[0] + 1, topple_coord[1])
        top_coord = (topple_coord[0], topple_coord[1] + 1)
        bottom_coord = (topple_coord[0], topple_coord[1] - 1)

        for coord_to_add_grain in [left_coord, right_coord, top_coord, bottom_coord]:
            if coord_to_add_grain not in piles:
                piles[coord_to_add_grain] = 0
            piles[coord_to_add_grain] += topple_times
            if piles[coord_to_add_grain] > 3:
                coords_to_topple.add(coord_to_add_grain)
    return num_topples

def plot_piles(piles):
    min_x = min([coord[0] for coord in piles])
    max_x = max([coord[0] for coord in piles])
    min_y = min([coord[1] for coord in piles])
    max_y = max([coord[1] for coord in piles])

    piles_arr = np.zeros((max_y - min_y + 1, max_x - min_x + 1))
    for (pile_x, pile_y), pile_size in piles.items():
        piles_arr[max_y - pile_y, pile_x - min_x] = pile_size

    plt.matshow(piles_arr)
    plt.show()

def simple_sandpile():
    sandpile = {}
    sandpile[(0, 0)] = 10000
    print(topple(sandpile))
    plot_piles(sandpile)

if __name__ == "__main__":
    simple_sandpile()