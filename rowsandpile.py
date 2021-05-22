# infinite size

import math
import timeit

import matplotlib.pyplot as plt
import numpy as np

def topple(piles: dict[int, int]):
    indexes_to_topple: set[int] = set()
    for pile_index, pile_size in piles.items():
        if pile_size >= 2:
            indexes_to_topple.add(pile_index)

    num_topples = 0
    while len(indexes_to_topple) > 0:
        # print(piles_to_arr(piles))
        # print(piles[0])
        topple_index = indexes_to_topple.pop()

        topple_times = piles[topple_index] // 2
        piles[topple_index] -= 2 * topple_times

        num_topples += topple_times

        left_index = topple_index - 1
        right_index = topple_index + 1

        for index_to_add_grain in [left_index, right_index]:
            if index_to_add_grain not in piles:
                piles[index_to_add_grain] = 0
            piles[index_to_add_grain] += topple_times
            if piles[index_to_add_grain] >= 2:
                indexes_to_topple.add(index_to_add_grain)
    return num_topples

def piles_to_arr(piles):
    min_x = min(piles)
    max_x = max(piles)

    piles_arr = np.zeros((max_x - min_x + 1))
    for pile_x, pile_size in piles.items():
        piles_arr[pile_x - min_x] = pile_size
    
    return piles_arr


def plot_piles(piles):

    print(piles_to_arr(piles))
    # plt.matshow(piles)
    # plt.show()

sandpile = {}
sandpile[0] = 100
print(topple(sandpile))
plot_piles(sandpile)

# x_points = list(range(0, 1000, 1))
# y_points = []

# piles: dict[tuple[int, int], int] = {}
# piles[(0, 0)] = 0
# total_piles = 0

# for center_pile_size in x_points:
#     total_piles += topple(piles)
#     y_points.append(total_piles)
#     piles[(0, 0)] += 10

# x = np.linspace(0, 1000, 100)
# # print(timeit.timeit(lambda: topple(piles), number=1))
# plt.plot(x_points, y_points)
# plt.plot(x, x**2.1)
# plt.show()
