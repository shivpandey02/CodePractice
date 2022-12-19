#include<iostream>
using namespace std;
void func1(int n){
    if(n==0){
        return;
    }
    cout<<n*2<<endl;

    func1(n-1);
}

int main(){
    int n;
    cin>>n;
    func1(n);
    return 0;
}