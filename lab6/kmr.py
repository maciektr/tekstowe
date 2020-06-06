import math


class Kmr:
    guard_char = '#'

    def __init__(self):
        pass

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

    def kmr(self, text):
        # original_length = len(text)
        # factor = math.floor(math.log2(len(text)))
        # max_lenght = 2 ** factor
        factor = Kmr.get_max_factor(len(text))
        padding_lenght = 2 ** (factor + 1) - 1
        text += Kmr.guard_char * padding_lenght
        position_to_index, first_entry = Kmr.sort_rename(list(text))
        names = {1: position_to_index}
        entries = {1: first_entry}
        for i in range(1, factor):
            power = 2 ** (i - 1)
            new_sequence = []
            for j in range(len(text)):
                if j+power < len(names[power]):
                    new_sequence.append((names[power][j], names[power][j+power]))
            position_to_index, first_entry = Kmr.sort_rename(new_sequence)
            names[power * 2] = position_to_index
            entries[power * 2] = first_entry
        return names, entries


if __name__ == '__main__':
    pass
