// recursive function to print the output
#include<iostream>
using namespace std;
int fun(int n){
    if(n==1){
        return 0;
    }
    else{
        return 1+fun(n/2);
    }
}

int main(){
    fun(16);
    
    return 0;
}
// output of this will be equal to 4 ...