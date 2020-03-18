#include<bits/stdc++.h>
using namespace std;

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
    string word;
    cin>>word;
    int *pi = new int[word.length()+1]; 
    make_pi(pi,word);
    delete[] pi;
}