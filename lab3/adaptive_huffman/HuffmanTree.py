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

    # def code(self):
    #     if self.parent is None:
    #         return bitarray()
    #     return self.parent.code() + (bitarray('1') if self.parent.right == self else bitarray('0'))

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

    # TU
    # def increment(self):
    #     self.weight += 1
    #     if self.parent is not None:
    #         self.parent.increment()
    #     if self.left is not None and self.right is not None:
    #         if self.left.weight > self.right.weight:
    #             Node.swap(self.left, self.right)
    #
    # def add_child(self, bit, node):
    #     node.parent = self
    #     if bit:
    #         self.right = node
    #     else:
    #         self.left = node
    #
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
        print('G ', node.char, ' ', code)
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
        print("ENC ", char)
        self.show()
        # print(self.get_code(self.init_char, self.root, bitarray()))

        if char in self.nodes:
            res = self.get_code(char, self.root, bitarray())
        else:
            res = self.get_code(self.init_char, self.root, bitarray())
            print("Init ", res)
            r = bitarray()
            r.frombytes(char.encode(self.encoding))
            res += r
        self.insert(char)
        print('res', res)
        return res

    def decode(self, bit):
        print(self.curr_node == self.root,'|', self.curr_node.char,'|', self.curr_node.left.char)
        self.show()
        self.curr_node = self.curr_node.right if bit else self.curr_node.left
        char = self.curr_node.char

        resp = {
            'char': None,
            'read_byte': False
        }

        print("REP /", char,'/')

        # if self.curr_node == self.get_zero_node():
        #     resp['read_byte'] = True
        #     self.curr_node = self.root
        # elif char is not None:
        #     resp['char'] = char
        #     self.curr_node = self.root

        if char is not None:
            if char == self.init_char:
                resp['read_byte'] = True
            else:
                resp['char'] = char
                self.insert(char)
            self.curr_node = self.root

        return resp

# TU
    def show(self):
        self.root.print()

# def decode(self, bit):
#     # node, char = self.curr_node.decode(bit)
#     node = self.curr_node.right if bit else self.curr_node.left
#     if node is not None:
#         print("DEC ", node.code(), ' ', node.char)
#     else:
#         print("DEC None")
#
#     char = None
#     if node is not None and node.char != self.init_char:
#         char = node.char
#     self.curr_node = node if node is not None else self.root
#
#     resp = {'char': char,
#             # 'read_byte': (node is not None) and (self.nodes[self.init_char] == node or node.char == self.init_char)}
#             'read_byte': (node is not None) and (self.nodes[self.init_char] == node)}
#     if resp['read_byte'] or resp['char'] is not None:
#         self.curr_node = self.root
#     return resp

# def next(self, char):
#     if char in self.nodes:
#         node = self.nodes[char]
#         # print('A: '+node.code().__str__() + ' ' + node.char)
#         # node.increment()
#         return self.nodes[char].code()
#     else:
#         r = bitarray()
#         r.frombytes(char.encode(self.encoding))
#         node = Node(char, weight=1)
#         zero_node = Node(self.init_char, weight=1, parent=self.get_zero_node().parent,
#                          left=self.get_zero_node(), right=node)
#         node.parent = zero_node
#         self.get_zero_node().parent = zero_node
#
#         if zero_node.parent is not None:
#             zero_node.parent.left = zero_node
#         else:
#             self.root = zero_node
#
#         self.register(zero_node)
#         self.register(node)
#         self.swap_order = [zero_node] + self.swap_order
#         self.swap_order = [node] + self.swap_order
#
#         k = zero_node.parent
#         while k is not None:
#             to_swap = None
#             for n in reversed(self.swap_order):
#                 if n.weight == k.weight:
#                     to_swap = n
#             if (k != to_swap) and (k != to_swap.parent) and (to_swap != k.parent):
#                 Node.swap(k, to_swap)
#                 k_id = self.swap_order.index(k)
#                 to_swap_id = self.swap_order.index(to_swap)
#                 self.swap_order[k_id], self.swap_order[to_swap_id] = self.swap_order[to_swap_id], self.swap_order[
#                     k_id]
#             k = k.parent
#
#         self.print()
#         return self.get_zero_node().code() + r

# 01100110 0 01101100 00 01101111 100 01110010 000011000011100001000001000011010010111101010100011101011010001101110110001000101001000001110100111000011001011000110101111111100101111010000001010
# 01100110 0 01101100 00 01101111 100 01110010 000011000011100001000001000011010010111101010100011101010000011011101010111110110101111100011101001100001100101000101011101001101011010000001010
# f          l           o            r                                                               TU