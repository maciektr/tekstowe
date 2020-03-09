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

void find(const string &word, const string &pattern, int* pi, vector<int> &index){
    int k = 0;

    for(int i = 0; i<(int)word.length(); i++){
        while(k > 0 && word[i] != pattern[k])
            k = pi[k-1];
        if(word[i] == pattern[k])
            k++;
        if(k == (int)pattern.size())
            index.push_back(i);
    }
}

void make_pi(int *pi, const string &pattern){
    int k = 0; 
    pi[0] = 0;
    for(int i =1; i<(int)pattern.length(); i++){
        while(k > 0 && pattern[k] != pattern[i])
            k = pi[k-1];
        if(pattern[k]==pattern[i])
            k++;
        pi[i] = k;
    }
}

int main(){
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    ifstream file(PATH);

    vector<match> result;
    string line;
    int line_index=1;

    int *pi = new int[PATTERN.length()+1]; 
    make_pi(pi,PATTERN);

    while(getline(file, line)){
        vector<int> index;
        find(line, PATTERN, pi, index);
        for(auto i : index)
            result.push_back(match(line_index, i));
        line_index++;
    }
    file.close();

    for(auto r : result)
        cout<<"line: "<<r.line<<"; index: "<<r.index<<'\n';
    cout<<"Found "<<result.size()<<" matches"<<endl;
    
    delete[] pi;
}