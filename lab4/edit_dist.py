from unidecode import unidecode
import numpy as np


def standard_delta(a, b):
    if a == b:
        return 0
    return 1


def unicode_delta(a, b):
    if a == b:
        return 0
    if unidecode(a) == unidecode(b):
        return 0.5
    return 1


def edit_distance(x, y, delta):
    edit_table = np.empty((len(x) + 1, len(y) + 1))
    for i in range(len(x) + 1):
        edit_table[i, 0] = i
    for j in range(len(y) + 1):
        edit_table[0, j] = j
    for i in range(len(x)):
        k = i + 1
        for j in range(len(y)):
            l = j + 1
            edit_table[k, l] = min(edit_table[k - 1, l] + 1,
                                   edit_table[k, l - 1] + 1,
                                   edit_table[k - 1, l - 1] + delta(x[i], y[j]))
    print(edit_table)
    return edit_table[len(x), len(y)]


if __name__ == '__main__':
    # a = 'los'
    # b = 'kloc'

    a = 'Łódź'
    b = 'Lodz'

    # a = 'kwintesencja'
    # b = 'quintessence'

    # a = 'ATGAATCTTACCGCCTCG'
    # b = 'ATGAGGCTCTGGCCCCTG'

    print(edit_distance(a, b, standard_delta))
