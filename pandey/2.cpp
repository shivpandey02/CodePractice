#include<iostream>
using namespace std;


int sumofDigits(int n){
    int sum=0;
    while(n>=0){
        sum=sum+n%10;
        n=n/10;
    }
    return sum;
}



int main(){
    int n ;
    cin>>n;
  cout<< sumofDigits(n);
  


    return 0 ;
}