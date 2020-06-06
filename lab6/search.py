from kmr import Kmr


def search(text, pattern):
    kmr = Kmr()
    pat_and_text = pattern + kmr.guard_char + text
    names, entries = kmr.kmr(pat_and_text)
    part_max_len = 2 ** Kmr.get_max_factor(len(pattern))
    res = []
    for i in range(len(pattern), len(names[part_max_len]) - len(pattern) + part_max_len):
        if names[part_max_len][0] == names[part_max_len][i] \
                and names[part_max_len][len(pattern) - part_max_len] == names[part_max_len][i + len(pattern) - part_max_len]:
            res.append(i-len(pattern)-1)
    return res


if __name__ == '__main__':
    pass
