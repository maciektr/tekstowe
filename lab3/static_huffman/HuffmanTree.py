from bitarray import bitarray


class HuffmanTree:
    class Node:
        def __init__(self, left, weight, right=None):
            self.left = left
            self.weight = weight
            self.right = right

        def __str__(self, h=1):
            if self.right is None:
                return '#' + str(self.weight) + ' ' + self.left

            res = '#' + str(self.weight) + '\n'
            res += ' ' * h + '0 -> ' + self.left.__str__(h + 1) + '\n'
            res += ' ' * h + '1 -> ' + self.right.__str__(h + 1)
            return res

        def is_leaf(self):
            return self.right is None

        def get_char(self):
            if not self.is_leaf():
                raise BaseException('This Node is not a leaf')
            return self.left

        def code(self, char, path=bitarray('')):
            if self.is_leaf():
                return path if self.left == char else None
            left_resp = self.left.code(char, path + bitarray('0'))
            if left_resp is not None:
                return left_resp
            return self.right.code(char, path + bitarray('1'))

        def decode(self, bit):
            if bit:
                if self.right.is_leaf():
                    return None, self.right.get_char()
                return self.right, None
            if self.left.is_leaf():
                return None, self.left.get_char()
            return self.left, None

    def __init__(self, letter_counts):
        nodes = []
        for a, weight in letter_counts.items():
            nodes.append(HuffmanTree.Node(a, weight))
        internal_nodes = []
        leafs = sorted(nodes, key=lambda n: n.weight)
        while len(leafs) + len(internal_nodes) > 1:
            head = []
            if len(leafs) >= 2:
                head += leafs[:2]
            elif len(leafs) == 1:
                head += leafs[:1]
            if len(internal_nodes) >= 2:
                head += internal_nodes[:2]
            elif len(internal_nodes) == 1:
                head += internal_nodes[:1]
            element_1, element_2 = sorted(head, key=lambda n: n.weight)[:2]
            internal_nodes.append(HuffmanTree.Node(element_1,
                                                   element_1.weight + element_2.weight,
                                                   element_2))
            if len(leafs) > 0 and element_1 == leafs[0]:
                leafs = leafs[1:]
            else:
                internal_nodes = internal_nodes[1:]
            if len(leafs) > 0 and element_2 == leafs[0]:
                leafs = leafs[1:]
            else:
                internal_nodes = internal_nodes[1:]
        self.root = internal_nodes[0]
        self.dec_node = self.root

    def get_root(self):
        return self.root

    def code(self, character):
        return self.get_root().code(character)

    def decode(self, bit):
        node, char = self.dec_node.decode(bit)
        self.dec_node = node if node is not None else self.root
        return char
