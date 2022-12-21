#include<iostream>
using namespace std;

int SumofNum(int n){
    if(n==0){
        return 0;
    }
    
    return SumofNum(n/10)+ n%10;
}


int main(){

    int n ;
    cin>>n;
  int ans=  SumofNum(n);
    cout<<ans;

    return 0;
}