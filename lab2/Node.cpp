//
// Created by maciektr on 06.04.2020.
//

#include "Node.h"

Node *Node::append(std::istream &in, bool (*ommit)(char)){
    char c;
    while(true)
        if(!(in>>c))
            return nullptr;
        else if (!ommit(c))
            break;

    if(!this->next.contains(c))
        this->next[c] = new Node(c);

    Node *ap = this->next[c]->append(in);
    return ap == nullptr ? this->next[c] : ap;
}
bool Node::isLeaf(){
    return this->next.empty();
}

#ifdef DEBUG
void Node::print_tree(int h){
    std::cout<<h<<": "<<this->letter<<std::endl;
    for(auto n : this->next)
        n.second->print_tree(h+1);
}
#endif