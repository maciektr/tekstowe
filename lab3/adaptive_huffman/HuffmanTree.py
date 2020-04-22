from collections import defaultdict
from bitarray import bitarray
import struct


class Node:
    def __init__(self, char, weight=None, parent=None):
        self.char = char
        self.weight = weight if weight is not None else 1
        self.parent = parent

        self.left = None
        self.right = None

    def code(self):
        if self.parent is None:
            return bitarray()
        # print("H ", self.parent.code(), (bitarray('1') if self.parent.right == self else bitarray('0')))
        return self.parent.code() + (bitarray('1') if self.parent.right == self else bitarray('0'))

    @staticmethod
    def swap(node1, node2):
        node1, node2 = node2, node1
        node1.parent, node2.parent = node2.parent, node1.parent

        if node1.parent.left is node2:
            node1.parent.left = node1
        else:
            node1.parent.right = node1

        if node2.parent.left is node1:
            node2.parent.left = node2
        else:
            node2.parent.right = node2

    def increment(self):
        self.weight += 1
        if self.parent is not None:
            self.parent.increment()
        if self.left is not None and self.right is not None:
            if self.left.weight > self.right.weight:
                Node.swap(self.left, self.right)

    def add_child(self, bit, node):
        node.parent = self
        if bit:
            self.right = node
        else:
            self.left = node

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
        self.nodes = {char: Node(char, 0)}
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
            node = Node(char, parent=updated_node)
            self.nodes[char] = node
            del self.nodes[self.init_char]
            zero_node = Node(self.init_char, parent=updated_node, weight=0)
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

    # TODO: Check inserting method
    def print(self):
        self.root.print()
        print("INIT ", self.nodes[self.init_char].code())
