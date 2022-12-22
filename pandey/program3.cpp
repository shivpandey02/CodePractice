// c++ program to swap two numbers.
#include<iostream>
using namespace std;
int swapnos(int *a , int *b ){
    int temp= *a;
        *a= *b;
        *b=temp;
    return *a , *b;
}
int main(){
    int x, y;
    cout<<"enter the first no "<<endl;
    cin>>x;
    cout<<"enter the second no "<<endl;
    cin>>y;
    cout<<" the two no before swapping are "<< x <<" and "<< y <<endl;
    swapnos(&x,&y);
    cout<<" the two no after the swapping will be "<< x << " and "<< y<< endl;

    


}