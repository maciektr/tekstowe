#include<bits/stdc++.h>
using namespace std;

// const char* PATH="1997_714.txt";
// const string PATTERN = "art";

const char* PATH="wikipedia-tail-kruszwil.txt";
const string PATTERN = "kruszwil";

// const char* PATH="a.txt";
// const string PATTERN = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";

struct match{
    int line;
    int index;
    match(int l, int i):line(l), index(i){}
};

void naive(const string &line,const string &pattern, vector<int> &index){
    for(int i = 0; i<(int)line.size()-(int)pattern.size(); i++)
        for(int k = 0; k<(int)pattern.size(); k++){
            if(line[i+k] != pattern[k])
                break;
            if(k==(int)pattern.size()-1 && line[i+k] == pattern[k])
                index.push_back(i);
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
        naive(line, PATTERN, index);
        for(auto i : index)
            result.push_back(match(line_index, i));
        line_index++;
    }
    file.close();

    for(auto r : result)
        cout<<"line: "<<r.line<<"; index: "<<r.index<<'\n';
    cout<<"Found "<<result.size()<<" matches"<<endl;
}