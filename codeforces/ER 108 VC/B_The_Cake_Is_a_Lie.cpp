#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0); 
    cin.tie(0);cout.tie(0); 

    int t;
    cin>>t;
    while(t--){

        int n,m,k;
        cin >> n >> m >> k;

        if (k == m*n -1) cout << "YES" << endl;
        else cout << "NO" << endl;

    }
    return 0;
}