//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// A Tree node
struct Node {
    int data;
    struct Node *left, *right;
};

// Utility function to create a new node
Node* newNode(int data) {
    Node* temp = new Node;
    temp->data = data;
    temp->left = temp->right = NULL;
    return (temp);
}

Node* buildTree(string str) {
    // Corner Case
    if (str.length() == 0 || str[0] == 'N')
        return NULL;

    // Creating vector of strings from input
    // string after spliting by space
    vector<string> ip;

    istringstream iss(str);
    for (string str; iss >> str;)
        ip.push_back(str);

    // Create the root of the tree
    Node* root = newNode(stoi(ip[0]));

    // Push the root to the queue
    queue<Node*> queue;
    queue.push(root);

    // Starting from the second element
    int i = 1;
    while (!queue.empty() && i < ip.size()) {

        // Get and remove the front of the queue
        Node* currNode = queue.front();
        queue.pop();

        // Get the current node's value from the string
        string currVal = ip[i];

        // If the left child is not null
        if (currVal != "N") {

            // Create the left child for the current node
            currNode->left = newNode(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->left);
        }

        // For the right child
        i++;
        if (i >= ip.size())
            break;
        currVal = ip[i];

        // If the right child is not null
        if (currVal != "N") {

            // Create the right child for the current node
            currNode->right = newNode(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->right);
        }
        i++;
    }

    return root;
}


// } Driver Code Ends
// User function Template for C++

/*// A Tree node
struct Node
{
    int data;
    struct Node *left, *right;
};*/

class Solution {
  public:
   static void merge(vector<int> &nodes,int low,int mid,int high,int &ans){
        int a = mid-low+1;
        int b = high-mid;
        int arr1[a];
        int arr2[b];
        for(int i=0;i<a;i++)arr1[i]=nodes[low+i];
        for(int i=0;i<b;i++)arr2[i]=nodes[mid+1+i];
        int i=0,j=0,k=low;
        while(i<a and j<b){
            if(arr1[i]<=arr2[j]){
                nodes[k]=arr1[i];
                i++;
            }
            else{
                ans+=a-i;
                nodes[k]=arr2[j];
                j++;
            }
            k++;
        }
        while(i<a){
            nodes[k++]=arr1[i++];
        }
        while(j<b){
            nodes[k++]=arr2[j++];
        }
    }
    static void mergesort(vector<int> &nodes,int low,int high,int &ans){
        if(low>=high)return;
        int mid = (low+high)/2;
        mergesort(nodes,low,mid,ans);
        mergesort(nodes,mid+1,high,ans);
        merge(nodes,low,mid,high,ans);
    }
    static void help(Node *root,vector<int> &nodes){
        if(!root)return;
        help(root->left,nodes);
        nodes.push_back(root->data);
        help(root->right,nodes);
    }
    /*You are required to complete below function */
    int pairsViolatingBST(int n, Node *root) {
        // your code goes here
        vector<int> nodes;
        help(root,nodes);
        int ans = 0;
        mergesort(nodes,0,n-1,ans);
        return ans;
    }
};


//{ Driver Code Starts.

int main() {

    int t;
    cin >> t;
    getchar();

    while (t--) {

        int n;
        cin >> n;
        getchar();

        string inp;
        getline(cin, inp);

        struct Node* root = buildTree(inp);

        Solution ob;
        int ans = ob.pairsViolatingBST(n, root);
        cout << ans << endl;
    }

    return 0;
}
// } Driver Code Ends
