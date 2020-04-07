#include <bits/stdc++.h>

using namespace std;

#include "Node.h"
#include "SuffixTrie.h"

int main() {
//    const string path = "../ustawa_250.txt";
    const string path = "../test/t.1";
    SuffixTrie::assertDelimiter(path.c_str());

    ifstream file(path);
    SuffixTrie trie(file, [](char c) { return !isalpha(c); });
    file.close();

    trie.root->print_tree();
}

