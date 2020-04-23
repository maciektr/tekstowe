from HuffmanTree import *
from bitarray import bitarray
import struct


class Compressor:
    def __init__(self, encoding='UTF-8', alhabet_size_type='I', characters_count_type='I'):
        self.encoding = encoding
        self.__alphabet_sizet = alhabet_size_type
        self.__dist_t = characters_count_type

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
            print(out_line)

    def decompress(self, file_path, out_path):
        tree = HuffmanTree()
        with open(file_path, 'rb') as file, open(out_path, 'w') as out:
            missing = struct.unpack('b', file.read(1))[0]
            bit_read = bitarray()
            bit_read.frombytes(file.read())
            # bit_read = bit_read[:(len(bit_read) - missing)]

            i = 0
            char = bit_read[i:i + 8].tobytes()
            char = char.decode(self.encoding)
            out.write(char)
            tree.insert(char)
            tree.curr_node = tree.root

            i += 8
            while i < len(bit_read) - missing:
                bit = bit_read[i]
                print('I', i, ' ', bit)
                resp = tree.decode(bit)
                i += 1
                if resp['read_byte'] and i + 8 < len(bit_read):
                    char = bit_read[i:i + 8].tobytes()
                    char = char.decode(self.encoding)
                    out.write(char)
                    tree.insert(char)
                    print("RED ", char)
                    i += 8
                elif resp['char'] is not None:
                    out.write(resp['char'])
                    print("DEC ", resp['char'])

    # def decompress(self, file_path, out_path):
    #     tree = HuffmanTree()
    #     with open(file_path, 'rb') as file, open(out_path, 'w') as out:
    #         missing = struct.unpack('b', file.read(1))[0]
    #         bit_read = bitarray()
    #         bit_read.frombytes(file.read())
    #         # print(bit_read[104:])
    #         i = 0
    #         char = bit_read[i:i + 8].tobytes()
    #         char = char.decode(self.encoding)
    #         out.write(char)
    #         tree.next(char)
    #         i += 8
    #         in_char = 0
    #         in_byte = 0
    #         tree.curr_node = tree.root
    #         while i < (len(bit_read) - missing):
    #             bit = bit_read[i]
    #             tree.print()
    #             resp = tree.decode(bit)
    #             if resp['char'] is not None:
    #                 out.write(resp['char'])
    #                 in_char += 1
    #             i += 1
    #             if resp['read_byte'] and i + 8 < len(bit_read):
    #                 char = bit_read[i:i + 8].tobytes()
    #                 char = char.decode(self.encoding)
    #                 out.write(char)
    #                 tree.next(char)
    #                 i += 8
    #                 in_byte += 1
# 01100110 0 01101100 00 01101111 100 01110010000011000011100001000001000011010010111101010100011101011010001101110110001000101001000001110100111000011001011000110101111111100101111010000001010
# 01100110 0 01101100 00 01101111     0111001000001100001001000000110100101110101000001101110011101000110010100000001010