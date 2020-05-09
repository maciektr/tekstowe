from unidecode import unidecode
from enum import Enum, auto
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


def edit_distance(x, y, delta=standard_delta):
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
    return edit_table[len(x), len(y)], edit_table


class Operation(Enum):
    REMOVE = auto()
    ADD = auto()
    CHANGE = auto()


def edit_sequence(a, b, edit_table=None):
    if edit_table is None:
        _, edit_table = edit_distance(a, b)
    else:
        if len(a) + 1 != len(edit_table) or len(b) + 1 != len(edit_table[0]):
            raise BaseException("Illegal argument: edit_table dimensions do not match words length.")

    x, y = len(a), len(b)
    h = []
    while x >= 0 and y >= 0:
        if x == 0 and y == 0:
            break
        if x - 1 >= 0 and y - 1 >= 0:
            if edit_table[x - 1][y - 1] <= edit_table[x][y - 1] and edit_table[x - 1][y - 1] <= edit_table[x - 1][y]:
                if not a[x - 1] == b[y - 1]:
                    h += [(Operation.CHANGE, (x - 1, y - 1), (a[x - 1], b[y - 1]))]
                x -= 1
                y -= 1
            elif edit_table[x][y - 1] < edit_table[x - 1][y - 1] and edit_table[x][y - 1] < edit_table[x - 1][y - 1]:
                y -= 1
                h += [(Operation.ADD, y, b[y])]
            elif edit_table[x - 1][y] < edit_table[x - 1][y - 1] and edit_table[x - 1][y] < edit_table[x - 1][y - 1]:
                x -= 1
                h += [(Operation.REMOVE, x, a[x])]
        elif x - 1 >= 0:
            x -= 1
            h += [(Operation.REMOVE, x, a[x])]
        elif y - 1 >= 0:
            y -= 1
            h += [(Operation.ADD, y, b[y])]

    return list(reversed(h))


def visualise(a, b):
    dist, table = edit_distance(a, b)
    sequence = edit_sequence(a, b, table)

    print('First word:', a, '\nSecond word:', b, '\nDistance: ', dist)
    change = 0
    for s in sequence:
        op, pos, char = s

        if op == Operation.REMOVE:
            p = pos + change
            q = pos + 1 + change
            print(a[:p] + '_' + a[q:])
            a = a[:p] + a[q:]
            change -= 1
        elif op == Operation.ADD:
            p = pos + change
            q = pos + 1 + change
            print(a[:p] + '+' + char + '+' + a[p:])
            a = a[:p] + char + a[p:]
            change += 1
        elif op == Operation.CHANGE:
            p = pos[0] + change
            q = pos[0] + 1 + change
            print(a[:p] + '*' + char[1] + '*' + a[q:])
            a = a[:p] + b[pos[1]] + a[q:]

    print("Finally: ", a)


if __name__ == '__main__':
    # a = 'los'
    # b = 'kloc'

    a = 'Łódź'
    b = 'Lodz'

    # a = 'kwintesencja'
    # b = 'quintessence'

    # a = 'ATGAATCTTACCGCCTCG'
    # b = 'ATGAGGCTCTGGCCCCTG'

    # dist, table = edit_distance(a, b)
    # print(table, dist)
    # print(edit_sequence(a, b, table))

    visualise(a, b)
