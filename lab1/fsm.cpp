#include<bits/stdc++.h>
using namespace std;

// const char* PATH="1997_714.txt";
// const string PATTERN = "art";

// const char* PATH="wikipedia-tail-kruszwil.txt";
// const string PATTERN = "kruszwil";

const char* PATH="ab.txt";
const string PATTERN = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB";

struct match{
    int line;
    int index;
    match(int l, int i):line(l), index(i){}
};

void find(const string &word, const string &pattern, vector<unordered_map<char, int> > &table, vector<int> &index){
    int q = 0; 
    for(int s = 0; s<(int)word.length(); s++){
        if(table[q].find(word[s]) != table[q].end())
            q = table[q][word[s]];
        else 
            q = 0;
        if(q == (int)pattern.length())
            index.push_back(s);
    }
}

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
    ifstream file(PATH);

    vector<match> result;
    string line;
    int line_index=1;

    vector<unordered_map<char, int> > table;
    transition_table(table, PATTERN);

    while(getline(file, line)){
        vector<int> index;
        find(line, PATTERN, table, index);
        for(auto i : index)
            result.push_back(match(line_index, i));
        line_index++;
    }
    file.close();

    for(auto r : result)
        cout<<"line: "<<r.line<<"; index: "<<r.index<<'\n';
    cout<<"Found "<<result.size()<<" matches"<<endl;
}