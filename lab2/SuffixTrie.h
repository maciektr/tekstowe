//
// Created by maciektr on 06.04.2020.
//

#ifndef LAB2_SUFFIXTRIE_H
#define LAB2_SUFFIXTRIE_H

#include "Node.h"

#include <iostream>
#include <fstream>
#include <sstream>

#define DEFAULT_MARK ' '

class SuffixTrie {
public:
    Node *root = nullptr;

    SuffixTrie(std::istream &input,bool (*func)(char)={[](char c){return false;}}, char mark_root=DEFAULT_MARK);
    static void assertDelimiter(const char *path);

private:
    bool (*ommit)(char) = [](char c){return false;};

    Node *last_leaf=nullptr;
};


#endif //LAB2_SUFFIXTRIE_H
