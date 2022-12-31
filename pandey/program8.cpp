// program to find if the year is leap or not 
#include<iostream>
using namespace std;
void leapyear( int n );
int main(){
    int year;
    cout<<" enter a year "<< endl;
    cin>>year;
    leapyear(year);
}
void leapyear( int n ){
    if (n%4 ==0)
    {
        cout<< n <<" is a leap year "<<endl;
    }
    else
    {
        cout<< n <<" is  not a leap year "<<endl;
        
    }
    
    
}