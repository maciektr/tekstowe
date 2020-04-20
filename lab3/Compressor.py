from HuffmanTree import HuffmanTree
from bitarray import bitarray
import struct


class Compressor:
    def __init__(self, encoding='UTF-8'):
        self.encoding = encoding
        self.__alphabet_sizet = 'I'
        self.__dist_t = 'H'

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
        # print(count)
        c_len = 0
        with open(file_path, 'wb') as file:
            chars_b = []
            for char in characters:
                c_b = char.encode(self.encoding)
                c_len += len(c_b)
                chars_b.append(c_b)
            file.write(struct.pack(self.__alphabet_sizet, c_len))
            # print(c_len)
            for c_b in chars_b:
                file.write(c_b)
            for char in characters:
                file.write(struct.pack(self.__dist_t, count[char]))

    def read_header(self, file_path):
        with open(file_path, 'rb') as file:
            n = struct.unpack(self.__alphabet_sizet, file.read(struct.calcsize(self.__alphabet_sizet)))[0]
            chars_b = file.read(n)
            characters = chars_b.decode(self.encoding)
            res = {}
            for char in characters:
                dist = struct.unpack(self.__dist_t, file.read(struct.calcsize(self.__dist_t)))[0]
                res[char] = dist
            seek_point = struct.calcsize(self.__alphabet_sizet) + n + len(characters) * struct.calcsize(self.__dist_t)
            return res , seek_point

    def compress(self, file_path, out_path):
        counts = self.count_in_file(file_path)
        tree = HuffmanTree(counts)
        self.write_header(out_path, counts)

        with open(file_path, 'r') as file, open(out_path, 'ab') as out:
            for line in file.readlines():
                out_line = bitarray()
                for word in line.split():
                    for char in word:
                        out_line += tree.code(char)
                out.write(out_line.tobytes())

        for c in map(lambda x: x[0], sorted(counts.items(), key=lambda x: -x[1])):
            print(c, tree.code(c))

    def decompress(self, file_path, out_path):
        counts, seek_point = self.read_header(file_path)
        # print(counts)
        tree = HuffmanTree(counts)
        print('--------------------------')
        for c in map(lambda x: x[0], sorted(counts.items(), key=lambda x: -x[1])):
            print(c, tree.code(c))

        with open(file_path, 'rb') as file, open(out_path, 'w') as out:
            file.seek(seek_point)
            bit_read = bitarray()
            bit_read.frombytes(file.read())
            print(bit_read)
            code = ''
            for bit in bit_read:
                code += '1' if bit else '0'

                resp = tree.decode(bit)
                if resp is not None:
                    out.write(resp)
                    code = ''
