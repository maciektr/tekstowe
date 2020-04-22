from collections import defaultdict
from bitarray import bitarray
import struct


class Node:
    def __init__(self, char, init_char, weight=None, parent=None):
        self.char = char
        self.weight = weight if weight is not None else 1
        self.parent = parent
        self.init_char = init_char

        self.left = None
        self.right = None

    def code(self):
        if self.parent is None:
            return bitarray()
        # print("H ", self.parent.code(), (bitarray('1') if self.parent.right == self else bitarray('0')))
        return self.parent.code() + (bitarray('1') if self.parent.right == self else bitarray('0'))

    def increment(self):
        self.weight += 1
        if self.parent is not None:
            self.parent.increment()
        if self.left is not None and self.right is not None:
            if self.left.weight > self.right.weight:
                self.left, self.right = self.right, self.left

    def add_child(self, bit, node):
        node.parent = self
        if bit:
            self.right = node
        else:
            self.left = node

    def decode(self, bit):
        if self.char != self.init_char:
            return None, self.char
        if bit:
            return self.right, None
        else:
            return self.left, None

    def print(self, h=0):
        print('H ', h, ': ', self.char)
        if self.left is not None:
            self.left.print(h + 1)
        if self.right is not None:
            self.right.print(h + 1)


class HuffmanTree:
    def __init__(self, char='#'):
        self.init_char = char
        self.count = defaultdict(int)
        self.nodes = {char: Node(char, self.init_char, 0)}
        self.root = self.nodes[char]
        self.curr_node = self.root
        self.encoding = 'UTF-8'

    def decode(self, bit):
        # node, char = self.curr_node.decode(bit)
        node = self.curr_node.right if bit else self.curr_node.left
        char = None
        if node is not None and node.char != self.init_char:
            char = node.char
        self.curr_node = node if node is not None else self.root

        resp = {'char': char, 'read_byte': node is not None and self.nodes[self.init_char] == node}
        if resp['read_byte'] or resp['char'] is not None:
            self.curr_node = self.root
        return resp

    def next(self, char):
        if char in self.nodes:
            node = self.nodes[char]
            # print('A: '+node.code().__str__() + ' ' + node.char)
            node.increment()
            return self.nodes[char].code()
        else:
            updated_node = self.nodes[self.init_char]
            a = updated_node.code()
            # print('B1: '+updated_node.code().__str__() + ' ' + updated_node.char)
            # print('B2: '+"{0:b}".format(ord(char)) + ' ' + char)
            node = Node(char, self.init_char, parent=updated_node)
            self.nodes[char] = node
            del self.nodes[self.init_char]
            zero_node = Node(self.init_char, self.init_char, parent=updated_node, weight=0)
            updated_node.add_child(0, zero_node)
            updated_node.add_child(1, node)
            self.nodes[self.init_char] = zero_node
            updated_node.increment()
            # return bitarray(bin(ord(char))[2:])
            r = bitarray()
            r.frombytes(char.encode(self.encoding))
            # print('CHAR ', char, ' ', self.nodes[self.init_char].code(), ' ', r)
            # self.print()
            return a + r

    def print(self):
        self.root.print()
        print("INIT ", self.nodes[self.init_char].code())
