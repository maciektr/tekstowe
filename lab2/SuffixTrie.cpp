//
// Created by maciektr on 06.04.2020.
//

#include "SuffixTrie.h"

void SuffixTrie::assertDelimiter(const char *const path) {
    std::fstream file(path);
    file.seekg(-2, std::fstream::end);
    char c;
    if (file >> c && isalpha(c)) {
        file.seekg(0, std::fstream::end);
        file << '#';
    }
    file.close();
}

SuffixTrie::SuffixTrie(std::istream &input,bool (*func)(char), const char mark_root) :ommit(func) {
    if (input.eof())
        return;
    Node *r = new Node(mark_root);
    input.seekg(-2, std::ifstream::end);
    int len = input.tellg();
    for (int i = 0; i <= len; i++) {
        input.clear();
        input.seekg(i, std::ifstream::beg);
        r->append(input, this->ommit);
    }
    this->root = r;
}