from HuffmanTree import HuffmanTree


class Compressor:
    def __init__(self):
        self.char_dist = {}
        pass

    def count_in_file(self, path):
        self.char_dist = {}
        with open(path, 'r') as f:
            for line in f.readlines():
                for word in line.split():
                    for char in word:
                        self.char_dist[char] = self.char_dist.get(char, 0) + 1

    def compress(self, file_path, out_path):
        self.count_in_file(file_path)
        tree = HuffmanTree(self.char_dist)
        with open(file_path, 'r') as file, open(out_path, 'w') as out:
            for line in file.readlines():
                for word in line.split():
                    for char in word:
                        pass
