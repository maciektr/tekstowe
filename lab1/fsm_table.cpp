#include<bits/stdc++.h>
using namespace std;

void transition_table(vector<unordered_map<char, int> > &table, const string &pattern){
    table.clear();
    table.push_back(unordered_map<char, int>());
    table[0][pattern[0]] = 1;
    int k = 0;
    for(int q = 1; q<=(int)pattern.length(); q++){
        table.push_back(table[k]);
        if(q < (int)pattern.length()){
            table[q][pattern[q]] = q+1;
            if(table[k].find(pattern[k]) != table[k].end())
                k = table[k][pattern[k]];
            else
                k = 0;
        }
    }   
}
int main(){
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    string word;
    cin>>word;
    vector<unordered_map<char, int> > table;
    transition_table(table,word);
}