#include<iostream>
using namespace std;

void func1(int n){
    if(n==0){
        return;
    }
    func1(n-1);
    cout<<n<<" ";
}

int main(){
    func1(5);



    return 0;
}