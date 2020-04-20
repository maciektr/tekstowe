from Compressor import *
from HuffmanTree import HuffmanTree

if __name__ == '__main__':
    comp = Compressor()

    comp.compress('../files/wiki_10kB.txt', 'out_comp.txt')
    comp.decompress('out_comp.txt', 'out_decomp.txt')
