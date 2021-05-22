import numpy as np
import matplotlib.pyplot as plt

import sandpiles as twodsp
import rowsandpile as onedsp

def piles_graph():
    x_points = list(range(0, 100, 1))
    y_1d_points = []
    y_2d_points = []

    piles_1d: dict[tuple[int, int], int] = {}
    piles_1d[0] = 0
    total_piles_1d = 0

    piles_2d: dict[tuple[int, int], int] = {}
    piles_2d[(0, 0)] = 0
    total_piles_2d = 0

    for center_pile_size in x_points:
        total_piles_1d += onedsp.topple(piles_1d)
        y_1d_points.append(total_piles_1d)
        piles_1d[0] += 1

        total_piles_2d += twodsp.topple(piles_2d)
        y_2d_points.append(total_piles_2d)
        piles_2d[(0, 0)] += 1

    x = np.linspace(0, 100, 100)
    # print(timeit.timeit(lambda: topple(piles), number=1))
    plt.plot(x_points, y_1d_points, label="1d")
    plt.plot(x_points, y_2d_points, label="2d")
    plt.legend()
    # plt.plot(x, x**1.4)
    plt.show()

if __name__ == "__main__":
    piles_graph()