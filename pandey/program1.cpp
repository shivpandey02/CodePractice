// c++ program to compute quoetient and reminder.
#include<iostream>
using namespace std;
int quotient( int a, int b );
int reminder( int a , int b );

int main(){
    int num1, num2,num3,num4;
    cout<<"enter the first number"<<endl;
    cin>>num1;
    cout<<"enter the second number"<<endl;
    cin>>num2;
    cout<<"enter the third number"<<endl;
    cin>>num3;
    cout<<"enter the fourth number for reminder "<<endl;
    cin>>num4;
    cout<<"the quoteint of the given first "<<num1<<"and second no "<<num2<< " is "<< quotient(num1,num2)<<endl;
    cout<<"the reminder  of the given first "<<num1<<"and second no "<<num2<< " is "<< reminder (num1,num2)<<endl;


}
int quotient( int num1, int num2){
    int quoteinthu = num1/num2;
    return quoteinthu;
    

}
int reminder( int num3 , int num4 ){
    int reminder = num3% num4;
    return reminder;
}
