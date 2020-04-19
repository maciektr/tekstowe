from HuffmanTree import HuffmanTree


class Compressor:
    def __init__(self):
        pass

    @staticmethod
    def count_in_file(path):
        char_dist = {}
        with open(path, 'r') as f:
            for line in f.readlines():
                for word in line.split():
                    for char in word:
                        char_dist[char] = char_dist.get(char, 0) + 1
        return char_dist

    def compress(self, file_path, out_path):
        tree = HuffmanTree(self.count_in_file(file_path))

        with open(file_path, 'r') as file, open(out_path, 'w') as out:
            for line in file.readlines():
                for word in line.split():
                    for char in word:
                        out.write(tree.code(char))
