#include<bits/stdc++.h>
using namespace std;
int main(){
    int len{0},ld{0},la{0};
    bool flag{false};
    vector<int> arr {};
    cin>>len;
    for(int i=0;i<len;i++){
        int temp;
        cin >> temp;
        arr.push_back(temp);
    }
    cin>>ld;
    la = INT_MIN;
    for(int i:arr){
        if(i>la and i%10==ld){
            flag = true;
            la = i;
        }
    }
    if(!flag) cout<<"-1";
    else cout << la;
    return 0;
}
