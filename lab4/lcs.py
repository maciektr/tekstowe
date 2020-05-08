from spacy.tokenizer import Tokenizer
from edit_dist import edit_distance
from spacy.lang.pl import Polish


def lcs(x, y):
    dist, table = edit_distance(x, y, lambda a, b: 0 if a == b else 2)
    result = []
    k, m = len(x), len(y)
    while k >= 0 and m >= 0 and not (k == 0 == m):
        if x[k - 1] == y[m - 1]:
            result.append(x[k - 1])
        if k - 1 >= 0 and m - 1 >= 0:
            if table[k - 1][m] < table[k][m - 1]:
                k -= 1
            else:
                m -= 1
        elif k - 1 >= 0:
            k -= 1
        elif m - 1 >= 0:
            m -= 1
    return (int(len(x) + len(y) - dist) // 2), list(reversed(result))


def tokenize_file(path):
    tokenizer = Tokenizer(Polish().vocab)
    with open(path, 'r') as file:
        text = ''.join(file.readlines())
        tokens = tokenizer(text)
    return list(tokens)


if __name__ == '__main__':
    path = 'romeo-i-julia-700.txt'
    # print(lcs(['aaa', 'bbbb', 'ccc'], ['aaa', 'dddd', 'bbbb', 'ccc']))
    # print(tokenize_file(path))
