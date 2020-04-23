from HuffmanTree import *
from bitarray import bitarray
import struct


class Compressor:
    def __init__(self, encoding='UTF-8'):
        self.encoding = encoding

    def compress(self, file_path, out_path):
        with open(file_path, 'r') as file, open(out_path, 'wb') as out:
            out_line = bitarray()
            char = file.read(1)
            tree = HuffmanTree()
            while char:
                out_line += tree.encode(char)
                char = file.read(1)

            missing = 8 - len(out_line) % 8
            out.write(struct.pack('b', missing))
            out.write(out_line.tobytes())

    def decompress(self, file_path, out_path):
        tree = HuffmanTree()
        with open(file_path, 'rb') as file, open(out_path, 'w') as out:
            missing = struct.unpack('b', file.read(1))[0]
            bit_read = bitarray()
            bit_read.frombytes(file.read())

            i = 0
            char = bit_read[i:i + 8].tobytes()
            char = char.decode(self.encoding)
            out.write(char)
            tree.insert(char)
            tree.curr_node = tree.root

            i += 8
            while i < len(bit_read) - missing:
                bit = bit_read[i]
                resp = tree.decode(bit)
                i += 1
                if resp['read_byte'] and i + 8 < len(bit_read):
                    char = bit_read[i:i + 8].tobytes()
                    char = char.decode(self.encoding)
                    out.write(char)
                    tree.insert(char)
                    i += 8
                elif resp['char'] is not None:
                    out.write(resp['char'])
