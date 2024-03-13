//{ Driver Code Starts

#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
/*You are required to complete this method */

class Solution{
  public:
    vector<int> matrixDiagonally(vector<vector<int>>&mat)
    {
         //Your code here
         int n=mat.size(),row=0,col=0;
         vector<int> ans;
         bool isReverse=false;
         while(col<n){
             int i=row,j=col;
             vector<int> temp;
             while(i<n and j<n and i>=0 and j>=0){
                 temp.push_back(mat[i][j]);
                 i--;
                 j++;
             }
             if(isReverse)reverse(temp.begin(),temp.end());
             ans.insert(ans.end(),temp.begin(),temp.end());
             if(row!=n-1){
                 row++;
                 col=0;
             }
             else{
                 col++;
             }
             isReverse=!isReverse;
         }
         return ans;
    }
};


//{ Driver Code Starts.
int main()
{
    int T;
    cin>>T;
  
    while(T--)
    {
        int n;
        int k=0;
        //cin>>k;
        cin>>n;
        vector<vector<int>>mat(n, vector<int>(n));
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                cin >> mat[i][j];
            }
        }
        Solution obj;
        vector<int>ans = obj.matrixDiagonally(mat);
        for(auto i: ans)cout << i << " ";
        cout << "\n";
        
       
    }
}
// } Driver Code Ends
