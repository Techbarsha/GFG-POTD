//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{

	public:
	
	int help(int i,int j,int n,int m,vector<vector<int>> &points,vector<vector<int>> &dp){
	    if(i==m-1 && j==n-1)return 1-points[i][j];
	    if(i==m or j==n)return INT_MAX;
	    if(dp[i][j]!=-1)return dp[i][j];
	    int a = help(i+1,j,n,m,points,dp);
	    int b = help(i,j+1,n,m,points,dp);
	    return dp[i][j] = max(1,min(a,b)-points[i][j]);
	}
	int minPoints(int m, int n, vector<vector<int>> points) 
	{ 
	    // Your code goes here
	    vector<vector<int>> dp(m,vector<int>(n,-1));
	    return help(0,0,n,m,points,dp);
	} 
};


//{ Driver Code Starts.
int main() 
{
   
   	int t;
    cin >> t;
    while (t--)
    {
        int m, n;
        cin >> m >> n;

        vector<vector<int>> a(m, vector<int>(n));

        for(int i = 0; i < m; i++)
        	for(int j = 0; j < n; j++)
        		cin >> a[i][j];

        

	    Solution ob;
	    cout << ob.minPoints(m,n,a) << "\n";
	     
    }
    return 0;
}

// } Driver Code Ends
