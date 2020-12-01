#include<bits/stdc++.h>
using namespace std;
int main(){
    int n {0};
    vector<int> arr;
    long long int avg {0};
    long long int ans {0};
    cin >> n;
    for(int j=0;j<n;j++){
        int t {0};
        cin >> t;
        arr.push_back(t);
    }
    sort(arr.begin(),arr.end());
    avg = arr[n/2];
    for(int e : arr){
        ans += abs(avg-e);
    }
    cout << ans <<"\n";
}
