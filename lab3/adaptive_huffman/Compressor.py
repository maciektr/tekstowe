from HuffmanTree import *
from bitarray import bitarray
import struct


class Compressor:
    def __init__(self, encoding='UTF-8', alhabet_size_type='I', characters_count_type='I'):
        self.encoding = encoding
        self.__alphabet_sizet = alhabet_size_type
        self.__dist_t = characters_count_type

    def compress(self, file_path, out_path):
        # tree = HuffmanTree()
        # self.write_header(out_path, counts)
        #
        with open(file_path, 'r') as file, open(out_path, 'wb') as out:
            out_line = bitarray()
            char = file.read(1)
            tree = HuffmanTree()
            while char:
                resp = tree.next(char)
                out_line += resp
                # print(char, ' = ', resp)
                char = file.read(1)
            out.write(out_line.tobytes())
            # print(out_line)

    def decompress(self, file_path, out_path):
        tree = HuffmanTree()
        with open(file_path, 'rb') as file, open(out_path, 'w') as out:
            bit_read = bitarray()
            bit_read.frombytes(file.read())

            i = 0
            char = bit_read[i:i + 8].tobytes()
            char = char.decode(self.encoding)
            out.write(char)
            tree.next(char)
            i += 8
            while i < len(bit_read):
                bit = bit_read[i]
                # print('I ', i, ' = ', bit_read[:i], ' = ', 1 if bit else 0)
                # tree.print()
                # print("CURR1 ", tree.curr_node.code(), " | ", tree.nodes['a'].code())
                resp = tree.decode(bit)
                # print("CURR2 ", tree.curr_node.code(), " | ", tree.nodes['a'].code())
                # print('RESP char ', resp['char'], 'read ', resp['read_byte'])
                if resp['char'] is not None:
                    # print('WRITE CHAR')
                    out.write(resp['char'])
                i += 1
                if resp['read_byte']:
                    # tree.print()
                    # print("READ BYTE ", bit_read[i:i + 8])
                    char = bit_read[i:i + 8].tobytes()
                    char = char.decode(self.encoding)
                    # print("BYTE: ", char, ' <- ', bit_read[i:i + 8])
                    out.write(char)
                    tree.next(char)
                    i += 8

# 01100001 0 01100010 00 01110010 0 100 01100011 011000110010001101100000000000100
# 01100001 0 01100010 00 01110010 0 100 01100011 011000110010001011001110000001010
# a          b           r        a     c

# 01100001 0 01100010 10 01110 010011001100011011100110010001011001111000001010
#   01100001 0  01100010 00  01110010 010001100011011000110010001101100000000000100
# 0 01100001 00 01100010 100 01110010 011000110001101110001100100010110011110000001010
