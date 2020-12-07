#include<bits/stdc++.h>
using namespace std;
int main(){
    int R{0},C{0},x1{0},y1{0},x2{0},y2{0};
    vector<vector<char>> matrix;
    cin >> R >> C;
    for(int i=0;i<R;i++){
        vector<char> temp;
        for(int j=0;j<C;j++){
            char t{};
            cin >> t;
            temp.push_back(t);
        }
        matrix.push_back(temp);
    }
    cin >> x1 >> y1 >> x2 >> y2;
    int x{x1-1},y{y1-1};
    while(true){
        if(x<R){
            for(x;x<R;x++){
                cout<<matrix.at(x).at(y);
                if(x==x2-1 and y==y2-1) return 0;
            }
        }
        if(x>=R){
            --x;
            ++y;
            for(x;x>=0;x--){
                cout<<matrix.at(x).at(y);
                if(x==x2-1 and y==y2-1) return 0;
            }
            x++;
            y++;
        }
    }
    cout<<endl;
    return 0;
}
