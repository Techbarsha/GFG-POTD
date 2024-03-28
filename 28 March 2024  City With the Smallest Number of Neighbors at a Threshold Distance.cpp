//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++
class Solution {
  public:
    int findCity(int n, int m, vector<vector<int>>& edges, int distanceThreshold) {
        // Your code here
         vector<pair<int,int>> adj[n];
        
        for(auto it : edges) {
            adj[it[0]].push_back({it[1],it[2]});
            adj[it[1]].push_back({it[0],it[2]});
        }
        vector<vector<int>> dist(n,vector<int>(n,INT_MAX));
        
        
        int minCity = INT_MAX;
        int ans = -1;
        
        for(int src = 0; src < n; src++) {
            dist[src][src] = 0;
            set<pair<int,int>> st;
            st.insert({0,src});
            
            while(!st.empty()) {
                auto it = *(st.begin());
                int wt = it.first;
                int node = it.second;
                st.erase(it);
                for(auto itr : adj[node]) {
                    int adjNode = itr.first;
                    int eWt = itr.second;
                    if(wt != INT_MAX && wt + eWt < dist[src][adjNode]) {
                        dist[src][adjNode] = wt + eWt;
                        st.insert({wt+eWt,adjNode});
                    }
                }
            }
            
            int count = 0;
            for(int j = 0; j < n; j++) {
                if(src != j && dist[src][j] <= distanceThreshold) count++;
            } 
            if(count <= minCity) {
                minCity = count;
                ans = src;
            }
        }
        
        return ans;
    }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<vector<int>> adj;
        // n--;
        for (int i = 0; i < m; ++i) {
            vector<int> temp;
            for (int j = 0; j < 3; ++j) {
                int x;
                cin >> x;
                temp.push_back(x);
            }
            adj.push_back(temp);
        }

        int dist;
        cin >> dist;
        Solution obj;
        cout << obj.findCity(n, m, adj, dist) << "\n";
    }
}

// } Driver Code Ends
