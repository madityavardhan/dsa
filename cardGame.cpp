#include<stdio.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int a,b,c,d,res=0;
        cin>>a>>b>>c>>d;
        // a,b suneet , c,d salvic
        if(a>c && b>=d) res++;
        if(a>d && b>=c) res++;
        if(b>c && a>=d) res++;
        if(b>d && a>=c) res++;
        // if(b>max(c,d)) res+=2;
        cout<<res<<"\n";
    }
}
