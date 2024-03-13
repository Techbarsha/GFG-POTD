//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution {
public:
    int largestSubsquare(int n, vector<vector<char>>& a) {
        vector<vector<int>> dp(n, vector<int>(n, 0)); // Declare dp matrix here
        int maxSize = 0;

        // Fill the first row and first column of dp matrix
        for (int i = 0; i < n; ++i) {
            dp[i][0] = (a[i][0] == 'X') ? 1 : 0;
            dp[0][i] = (a[0][i] == 'X') ? 1 : 0;
            maxSize = max(maxSize, dp[i][0]);
            maxSize = max(maxSize, dp[0][i]);
        }

        // Fill the rest of the dp matrix
        for (int i = 1; i < n; ++i) {
            for (int j = 1; j < n; ++j) {
                if (a[i][j] == 'X') {
                    dp[i][j] = 1 + min({dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]});
                    maxSize = max(maxSize, dp[i][j]);
                }
            }
        }

        return maxSize;
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<vector<char>> a(n, vector<char>(n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) cin >> a[i][j];
        }
        Solution ob;
        cout << ob.largestSubsquare(n, a) << "\n";
    }
}
// } Driver Code Ends
