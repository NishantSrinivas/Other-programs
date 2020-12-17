#include<bits/stdc++.h>
using namespace std;
int main(){
    string s1 {},s2 {};
    getline(cin,s1);
    getline(cin,s2);
    int s1_size {s1.size()},start_idx {0},end_idx {s1_size-1};
    for(int i=0;i<s1_size;i++){
        if(s1.at(i)!=s2.at(i)){
            break;
        } 
        else{
            start_idx++;
        }
    }
    for(int j=s1_size-1;j>0;j--){
        if(s1.at(j)!=s2.at(j)){
            break;
        }
        else{
            end_idx--;
        }
    }
    cout<<s1.substr(start_idx,(end_idx-start_idx)+1)<<"\n";
    return 0;
}
