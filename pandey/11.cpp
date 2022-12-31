#include<iostream>
using namespace std;

bool recursiveSearch(int arr[],int l, int r,int x){
    if(arr[l]==x || arr[r]==x){
        return true;
    }
    if(r<l){
        return false;
    }
    recursiveSearch(arr,l+1,r-1,x);
}

int main(){
    int arr[100];
    int x,r,l;

    for(int i =0;i<5;i++){
        cin>>arr[i];
    }
    x=66;
    r=4;
    l=0;
    recursiveSearch(arr,l,r,x);
    return 0;
}