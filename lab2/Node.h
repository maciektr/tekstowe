//
// Created by maciektr on 06.04.2020.
//

#ifndef LAB2_NODE_H
#define LAB2_NODE_H

#include <unordered_map>
#include <iostream>

class Node {
public:
    Node(char c) : letter(c) {}

    Node *append(std::istream &in, bool (*ommit)(char) = {[](char c) { return false; }});
    bool isLeaf();

#ifdef DEBUG
    void print_tree(int h = 0);
#endif

protected:
    char letter;
    std::unordered_map<char, Node *> next;
};


#endif //LAB2_NODE_H
