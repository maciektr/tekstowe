//
// Created by maciektr on 06.04.2020.
//

#include "Node.h"

void Node::append(std::istream &in, bool (*ommit)(char)){
    char c;
//    std::cout<<"AP"<<std::endl;
    while(true)
        if(!(in>>c))
            return;
        else if (!ommit(c))
            break;
    std::cout<<c;
    if(!this->next.contains(c)) {
        Node *nnn = new Node(c);
        this->next[c] = nnn;
    }
    this->next[c]->append(in);
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