class Solution{
  public:
    int MissingNumber(vector<int>& array, int n) {
        // Your code goes here
        sort(array.begin(),array.end());
        for(int i =1;i<n;i++){
            if(array[0]!=1){
                return 1;
            }
        
        else if(array[i]!=array[i-1]+1){
            return (array[i-1]+1);
        }
        }
    }
};