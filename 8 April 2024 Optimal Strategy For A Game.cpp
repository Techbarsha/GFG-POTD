//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

//Function to find the maximum possible amount of money we can win.
class Solution{
    public:
    long long solve(int arr[], int left, int right, vector<vector<long long>>&dp){
        if(left>right) return 0;
        if(left==right) return arr[left];
        if(dp[left][right]!=-1) return dp[left][right];
        
        long long l=arr[left]+min(solve(arr, left+2, right, dp), solve(arr, left+1, right-1,dp));
        long long r=arr[right]+min(solve(arr, left, right-2, dp), solve(arr, left+1, right-1,dp));
        
        return dp[left][right] = max(l,r);
    }
    
    long long maximumAmount(int n, int arr[]){
        // Your code here
        vector<vector<long long>>dp(n+1, vector<long long>(n+1, -1));
        long long ans=solve(arr, 0, n-1, dp);
        return ans;
    }
};

//{ Driver Code Starts.
int main() 
{
   
   	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		int a[n];
		for(int i=0;i<n;i++)
		cin>>a[i];
		Solution ob;
		cout<< ob.maximumAmount(n,a)<<endl;
	}
	return 0;
}
// } Driver Code Ends
