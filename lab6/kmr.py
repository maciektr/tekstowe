import math


class Kmr:
    guard_char = '#'

    def __init__(self, guard_char='#'):
        if guard_char is not None:
            Kmr.guard_char = guard_char
            self.names = None
            self.entries = None
            self.text = None

    @staticmethod
    def sort_rename(sequence):
        last_entry = None
        index = 0
        position_to_index = [None] * len(sequence)
        first_entry = {}
        for entry in sorted([(e,i) for i,e in enumerate(sequence)]):
            if last_entry and last_entry[0] != entry[0]:
                index += 1
                first_entry[index] = entry[1]
            position_to_index[entry[1]] = index
            if last_entry is None:
                first_entry[0] = entry[1]
            last_entry = entry
        return position_to_index, first_entry

    @staticmethod
    def get_max_factor(n):
        return math.floor(math.log2(n))

    def kmr(self, text, stop_at=None):
        if self.text == text and self.names is not None and self.entries is not None:
            return self.names, self.entries
        self.text = text

        factor = Kmr.get_max_factor(len(text))
        padding_lenght = 2 ** (factor + 1) - 1
        text += Kmr.guard_char * padding_lenght
        position_to_index, first_entry = Kmr.sort_rename(list(text))
        names = {1: position_to_index}
        entries = {1: first_entry}
        for i in range(1, factor if stop_at is None or stop_at >= factor else stop_at):
            power = 2 ** (i - 1)
            new_sequence = []
            for j in range(len(text)):
                if j+power < len(names[power]):
                    new_sequence.append((names[power][j], names[power][j+power]))
            position_to_index, first_entry = Kmr.sort_rename(new_sequence)
            names[power * 2] = position_to_index
            entries[power * 2] = first_entry

        self.names = names
        self.entries = entries
        return self.names, self.entries

    def search(self, text, pattern):
        if len(pattern) > len(text):
            raise Exception("Pattern len cannot exceed text len.")

        pat_and_text = pattern + Kmr.guard_char + text
        max_pat_factor = max(1, Kmr.get_max_factor(len(pattern)) * 2)
        if self.names is None or self.entries is None:
            self.kmr(pat_and_text, stop_at=max_pat_factor)

        part_max_len = 2 ** Kmr.get_max_factor(len(pattern))
        res = []
        for i in range(len(pattern), len(self.names[part_max_len]) - len(pattern) + part_max_len):
            if self.names[part_max_len][0] == self.names[part_max_len][i] \
                    and self.names[part_max_len][len(pattern) - part_max_len] == self.names[part_max_len][i + len(pattern) - part_max_len]:
                res.append(i-len(pattern)-1)
        return res


if __name__ == '__main__':
    pass
