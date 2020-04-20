from HuffmanTree import HuffmanTree
from bitarray import bitarray
import struct


class Compressor:
    def __init__(self, encoding='UTF-8'):
        self.encoding = encoding
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

    def write_header(self, file_path, count):
        characters = list(map(lambda x: x[0], reversed(sorted([(a, w) for a, w in count.items()], key=lambda x: x[1]))))
        print(characters)
        c_len = 0
        with open(file_path, 'wb') as file:
            chars_b = []
            for char in characters:
                c_b = char.encode(self.encoding)
                c_len += len(c_b)
                chars_b.append(c_b)
            file.write(struct.pack('i', c_len))
            for c_b in chars_b:
                file.write(c_b)

    def read_header(self, file_path):
        with open(file_path, 'rb') as file:
            n = struct.unpack('i', file.read(4))[0]
            chars_b = file.read(n)
            characters = chars_b.decode(self.encoding)
            i = 0
            res = {}
            for char in reversed(characters):
                res[char] = i
                i += 1
            return res

    def compress(self, file_path, out_path):
        counts = self.count_in_file(file_path)
        tree = HuffmanTree(counts)
        self.write_header(out_path, counts)

        with open(file_path, 'r') as file, open(out_path, 'wb+') as out:
            for line in file.readlines():
                out_line = bitarray()
                for word in line.split():
                    for char in word:
                        out_line += tree.code(char)
                out.write(out_line.tobytes())

    def decompress(self, file_path, out_path):
        counts = self.read_header(file_path)
        tree = HuffmanTree(counts)

        with open(file_path, 'rb') as file, open(out_path, 'w') as out:
            pass 

