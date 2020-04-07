cmake_minimum_required(VERSION 3.15)
project(lab2)

set(CMAKE_CXX_STANDARD 20)
add_definitions(-DDEBUG)
add_executable(trie trie.cpp Node.cpp Node.h SuffixTrie.cpp SuffixTrie.h)
add_executable(creight creight.cpp Node.cpp Node.h SuffixTrie.cpp SuffixTrie.h)