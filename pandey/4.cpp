// recursively calling different elements and printing in a way to produce a output
#include<iostream>
using namespace std;
void fun(int n){
    if(n==0)
     return;
     fun(n-1);
     cout<<n<<endl;
     fun(n-1);
}

int main(){
    fun(3);

    return 0;
}
// output for this will be 1 2 1 3 1 2 1 