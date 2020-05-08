from lcs import lcs, tokenize_file
import argparse


def diff(path1, path2):
    tokens1 = tokenize_file(path1)
    print(tokens1[665:685])
    tokens2 = tokenize_file(path2)
    print(tokens2[665:685])

    _, same = lcs(tokens1, tokens2)
    print(same[675:695])
    last1, last2 = 0, 0
    act1, act2 = 0, 0
    lcs_ind, line_ind = 0, 0
    show = False
    while act1 < len(tokens1) and act2 < len(tokens2):
        if not tokens2[act2] == same[lcs_ind]:
            act2 += 1
            show = True
            continue
        elif not tokens1[act1] == same[lcs_ind]:
            act1 += 1
            show = True
            continue
        if same[lcs_ind][:1] == '\n' or tokens1[act1][:1] == '\n' or tokens2[act2][:1] == '\n':
            print("NNN", act1, [tokens1[act1]], act2, [tokens2[act2]])
            if show:
                print("Difference in line", line_ind + 1)
                # print("<", ' '.join(tokens1[last1:act1]))
                # print(">", ' '.join(tokens2[last2:act2]))
                print("<", tokens1[last1:act1])
                print(">", tokens2[last2:act2])
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
