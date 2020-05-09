from lcs import lcs, tokenize_file
import argparse


def split_element(arr, index, pos):
    arr.insert(index + 1, arr[index][pos:])
    arr[index] = arr[index][:pos]


def diff(path1, path2):
    delta = lambda a, b: 0 if a == b or a[:1] == b[:1] == '\n' else 2

    tokens1 = tokenize_file(path1)
    tokens2 = tokenize_file(path2)
    _, same = lcs(tokens1, tokens2, delta)

    last1, last2 = 0, 0
    act1, act2 = 0, 0
    lcs_ind, line_ind = 0, 0
    show = False
    first_shift = True
    while act1 < len(tokens1) and act2 < len(tokens2):
        if not delta(tokens2[act2], same[lcs_ind]) == 0:
            act2 += 1
            show = True
            continue
        elif not delta(tokens1[act1], same[lcs_ind]) == 0:
            act1 += 1
            show = True
            continue

        if same[lcs_ind][:1] == '\n':
            if not len(tokens1[act1]) == len(tokens2[act2]):
                if len(tokens1[act1]) > len(tokens2[act2]):
                    split_element(tokens1, act1, len(tokens2[act2]))
                    same.insert(lcs_ind + 1, tokens1[act1 + 1])
                    tokens1.insert(act1 + 1, '')
                elif len(tokens1[act1]) < len(tokens2[act2]):
                    split_element(tokens2, act2, len(tokens1[act1]))
                    same.insert(lcs_ind + 1, tokens2[act2 + 1])
                    tokens2.insert(act2 + 1, '')

                if not first_shift:
                    line_ind += 1
                else:
                    first_shift = False

            if show:
                print("Difference in line", line_ind + 1)
                print("<", ' '.join(tokens1[last1:act1]))
                print(">", ' '.join(tokens2[last2:act2]))
            show = False
            line_ind += same[lcs_ind].count('\n')
            last1 = act1 + 1
            last2 = act2 + 1
            act1 += 1
            act2 += 1
            lcs_ind += 1
            continue

        act1 += 1
        act2 += 1
        lcs_ind += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Diff - compare files line by line.')
    parser.add_argument('path', metavar='P', type=str, nargs=2,
                        help='path to text file')
    args = parser.parse_args()
    path1 = args.path[0]
    path2 = args.path[1]

    diff(path1, path2)
