// #include<bits/stdc++.h>
#include <iostream>
#include <vector>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n,m,s,prev=0,flag=0;
        cin>>n>>m>>s;
        // vector<pair<int,int>> intervels;
        for(int i=0;i<n;i++){
            int i1,i2;
            cin>>i1>>i2;
            // cout<<i1<<" "<<i2<<" "<<i1-prev+1<<" "<<m<<" "<<"\n";
            if(i1-prev+1 >= m){
                flag=1;
            } 
            prev=i2;
        }
        // cout<<s-prev+1<<" ";
        if(s-prev>=m){
            flag=1;
        }
        cout<<((flag)?"YES\n":"NO\n");
    }
}
