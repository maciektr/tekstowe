from collections import defaultdict
from bitarray import bitarray
import struct


class Node:
    def __init__(self, char, weight=None, parent=None, left=None, right=None):
        self.char = char
        self.weight = weight if weight is not None else 1
        self.parent = parent
        self.left = left
        self.right = right

    @staticmethod
    def swap(node1, node2):
        node1.parent, node2.parent = node2.parent, node1.parent

        if node1.parent.left == node2:
            node1.parent.left = node1
        else:
            node1.parent.right = node1

        if node2.parent.left == node1:
            node2.parent.left = node2
        else:
            node2.parent.right = node2

    def print(self, h=0):
        print('H ', h, ': ', self.char)
        if self.left is not None:
            self.left.print(h + 1)
        if self.right is not None:
            self.right.print(h + 1)


class HuffmanTree:
    def __init__(self, char='#'):
        self.init_char = char
        self.nodes = {char: Node(char, 0)}
        self.root = self.get_zero_node()
        self.encoding = 'UTF-8'
        self.swap_order = []
        self.curr_node = self.root

    def get_zero_node(self):
        return self.nodes[self.init_char]

    @staticmethod
    def get_code(char, node, code=bitarray('')):
        if node.left is None and node.right is None:
            return code if node.char == char else bitarray()
        else:
            t = bitarray()
            if node.left is not None:
                t += HuffmanTree.get_code(char, node.left, code + bitarray('0'))
            if node.right is not None:
                t += HuffmanTree.get_code(char, node.right, code + bitarray('1'))
            return t

    def find_to_swap(self, weight):
        for n in reversed(self.swap_order):
            if n.weight == weight:
                return n

    def swap_nodes(self, node1, node2):
        n1_id = self.swap_order.index(node1)
        n2_id = self.swap_order.index(node2)
        self.swap_order[n1_id], self.swap_order[n2_id] = self.swap_order[n2_id], self.swap_order[n1_id]

        Node.swap(node1, node2)

    def register(self, node):
        self.nodes[node.char] = node

    def insert(self, char):
        if char not in self.nodes:
            node = Node(char)
            zero_node = Node(None, parent=self.get_zero_node().parent, left=self.get_zero_node(), right=node)
            node.parent = zero_node
            self.get_zero_node().parent = zero_node

            if zero_node.parent is not None:
                zero_node.parent.left = zero_node
            else:
                self.root = zero_node

            self.swap_order = [node, zero_node] + self.swap_order
            self.register(node)

            n = zero_node.parent
            while n is not None:
                k = self.find_to_swap(n.weight)
                if (n != k) and (n != k.parent) and (k != n.parent):
                    self.swap_nodes(n, k)
                n.weight += 1
                n = n.parent

    def encode(self, char):
        if char in self.nodes:
            res = self.get_code(char, self.root, bitarray())
        else:
            res = self.get_code(self.init_char, self.root, bitarray())
            r = bitarray()
            r.frombytes(char.encode(self.encoding))
            res += r
        self.insert(char)
        return res

    def decode(self, bit):
        self.curr_node = self.curr_node.right if bit else self.curr_node.left
        char = self.curr_node.char

        resp = {
            'char': None,
            'read_byte': False
        }

        if char is not None:
            if char == self.init_char:
                resp['read_byte'] = True
            else:
                resp['char'] = char
                self.insert(char)
            self.curr_node = self.root

        return resp
