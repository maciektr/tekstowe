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
                x = bitarray()
                x.frombytes(char.encode(self.encoding))
                # print('|', char, '| = ', resp, char.encode(self.encoding), x)
                char = file.read(1)

            missing = 8 - len(out_line) % 8
            # print('missing', missing)
            out.write(struct.pack('b', missing))
            out.write(out_line.tobytes())
            # print(out_line)

    def decompress(self, file_path, out_path):
        tree = HuffmanTree()
        with open(file_path, 'rb') as file, open(out_path, 'w') as out:
            missing = struct.unpack('b', file.read(1))[0]
            bit_read = bitarray()
            bit_read.frombytes(file.read())
            # print(bit_read[104:])

            i = 0
            char = bit_read[i:i + 8].tobytes()
            char = char.decode(self.encoding)
            out.write(char)
            tree.next(char)
            i += 8
            in_char = 0
            in_byte = 0
            while i < (len(bit_read) - missing):
                bit = bit_read[i]
                # print('--I ', i, ' = ', 1 if bit else 0)
                # tree.print()
                # print("CURR1 ", tree.curr_node.code())
                resp = tree.decode(bit)
                # print("CURR2 ", tree.curr_node.code(), " | ", tree.nodes['a'].code())
                # print('RESP char ', resp['char'], 'read ', resp['read_byte'])
                if resp['char'] is not None:
                    # print('WRITE CHAR ', resp['char'], ' <--')
                    out.write(resp['char'])
                    in_char +=1
                i += 1
                if resp['read_byte'] and i + 8 < len(bit_read):
                    # tree.print()
                    # print("READ BYTE ", bit_read[i:i + 8])
                    char = bit_read[i:i + 8].tobytes()
                    char = char.decode(self.encoding)
                    # print("BYTE: ", char, ' <- ', bit_read[i:i + 8])
                    out.write(char)
                    tree.next(char)
                    i += 8
                    in_byte +=1
