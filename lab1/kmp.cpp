#include<bits/stdc++.h>
using namespace std;

// const char* PATH="1997_714.txt";
// const string PATTERN = "art";

const char* PATH="wikipedia-tail-kruszwil.txt";
const string PATTERN = "kruszwil";

struct match{
    int line;
    int index;
    match(int l, int i):line(l), index(i){}
};

void find(const string &line, const string &pattern, vector<int> &index){
    string word = pattern+'#'+ line;

    vector<int> tab;
    tab.resize(word.length(),0);
    int k = 0;
    for(int i = 1; (unsigned)i<word.length(); i++){
        while(k > 0 && word[i] != word[k])
            k = tab[k-1];
        if(word[i] == word[k])
            k++;
        tab[i] = k;
        if(tab[i] == (int)pattern.size())
            index.push_back(i-pattern.size()-1);
    }
}


int main(){
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    ifstream file(PATH);

    vector<match> result;
    string line;
    int line_index=1;
    while(getline(file, line)){
        vector<int> index;
        find(line, PATTERN, index);
        for(auto i : index)
            result.push_back(match(line_index, i));
        line_index++;
    }
    file.close();

    for(auto r : result)
        cout<<"line: "<<r.line<<"; index: "<<r.index<<'\n';
    cout<<"Found "<<result.size()<<" matches"<<endl;
}