from spacy.tokenizer import Tokenizer
from edit_dist import edit_distance
from spacy.lang.pl import Polish
from random import randint


def lcs(x, y):
    if len(x) == 0 or len(y) == 0:
        return 0, []

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
    return list(map(str, tokens))


def remove_random(arr, number):
    arr = list(arr)
    while number >= 0:
        r = randint(0, len(arr) - 1)
        if not str(arr[r]).isalnum():
            continue
        print('REM', arr[r])
        arr.pop(r)
        number -= 1
    return arr


def write_as_file(tokens, path):
    tokens = list(map(lambda x: str(x), tokens))
    with open(path, 'w') as file:
        size = len(tokens)
        idx_list = [idx + 1 for idx, val in
                    enumerate(tokens) if val[:1] == '\n']

        lines = [tokens[i: j] for i, j in
                 zip([0] + idx_list, idx_list +
                     ([size] if idx_list[-1] != size else []))]
        file.write(''.join(map(lambda line: ' '.join(line), lines)))


if __name__ == '__main__':
    path = 'romeo-i-julia-700.txt'
    path1 = 'romeo_i_julia_1.txt'
    path2 = 'romeo_i_julia_2.txt'

    # print(lcs(['aaa', 'bbbb', 'ccc'], ['aaa', 'dddd', 'bbbb', 'ccc']))

    # tokens = tokenize_file(path)
    # len(tokens)
    # tokens_1 = remove_random(tokens, len(tokens) * 3 // 100)
    # write_as_file(tokens_1, path1)
    # tokens_2 = remove_random(tokens, len(tokens) * 3 // 100)
    # write_as_file(tokens_2, path2)

    tokens_1 = tokenize_file(path1)
    # print(tokens_1)
    tokens_2 = tokenize_file(path2)
    # print(tokens_2)
    # print('|' + str(tokens_1[0])+'|'+str(tokens_2[0])+'|', tokens_1[0] == tokens_2[0])
    print(lcs(tokens_1, tokens_2))
