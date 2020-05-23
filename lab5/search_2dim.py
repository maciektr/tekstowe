from lab5.aho import AhoCorasick
import numpy as np


def lines_to_matrix(lines):
    max_line_len = max([len(line) for line in lines])
    for i in range(len(lines)):
        line = lines[i]
        for _ in range(max_line_len - len(line)):
            line += '\0'
        lines[i] = np.array(list(line))
    return np.vstack(lines)


def search_2dim(text, pattern):
    text = lines_to_matrix(text)
    pattern = lines_to_matrix(pattern)
    pattern_columns = [pattern[:, k] for k in range(pattern.shape[1])]

    aho = AhoCorasick(pattern_columns)
    transition = aho.transition
    output = aho.output

    states = np.zeros(text.shape)
    for k in range(states.shape[1]):
        for i in range(states.shape[0]):
            states[i, k] = transition[int(states[i - 1, k])][text[i, k]]

    pattern_columns = list(map(''.join, pattern_columns))
    result = []
    for i in range(states.shape[0]):
        for k in range(states.shape[1] - len(pattern_columns)):
            res = True
            for m in range(len(pattern_columns)):
                pat = pattern_columns[m]
                if pat not in output[int(states[i, k + m])]:
                    res = False
            if res:
                result.append((i - pattern.shape[0] + 1, k))

    return result


if __name__ == '__main__':
    text = ["abababb",
            "aaaabbb",
            "bbbaaab",
            "aaabbaa",
            "bbaaabb",
            "aabaaaa"]
    pat = ["aaa", "bba", "aab"]
    print(search_2dim(text, pat))
