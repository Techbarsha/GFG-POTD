//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

struct Node
{
	int data;
	struct Node *next;
	
	Node(int x){
	    data =x;
	    next = NULL;
	}
};
/* Function to print linked list */


void append(struct Node** headRef, struct Node** tailRef, int newData)
{
	struct Node* new_node = new Node(newData);
	struct Node *last = *headRef;
	if (*headRef == NULL)
	{
	    *headRef = new_node;
	    *tailRef = *headRef;
	    return;
	}
	
	(*tailRef) -> next = new_node;
	*tailRef = (*tailRef) -> next;
}

// A utility function to print a linked list
void printList(Node *head)
{
	while (head != NULL)
	{
		cout << head->data << " ";
		head = head->next;
	}
	cout << endl;
}



// } Driver Code Ends

/*
struct Node
{
	int data;
	struct Node *next;
	
	Node(int x){
	    data =x;
	    next = NULL;
	}
};
*/

class Solution
{
    public:
    // your task is to complete this function
    void sort(Node **head)
    {
         // Code here
         Node *head1=new Node(0),*head2=new Node(0);
         Node *temp1=head1,*temp2=head2,*temp=*head;
         bool indication=true;
         while(temp){
             if(indication){
                 temp1->next=temp;
                 temp1=temp1->next;
             }
             else{
                 temp2->next=temp;
                 temp2=temp2->next;
             }
             temp=temp->next;
             indication=!indication;
         }
         temp1->next=NULL;
         temp2->next=NULL;
         Node *curr=head2,*prev=NULL,*nxt=head2->next;
         while(curr){
             nxt=curr->next;
             curr->next=prev;
             prev=curr;
             curr=nxt;
         }
         temp=prev;
         while(prev){
             if(prev->next==head2){
                 prev->next=NULL;
             }
             prev=prev->next;
         }
         Node *ans = new Node(0);
         head2=ans;
         head1=head1->next;
         while(head1 and temp){
             if(head1->data<=temp->data){
                 ans->next=head1;
                 head1=head1->next;
             }
             else{
                 ans->next=temp;
                 temp=temp->next;
             }
             ans=ans->next;
         }
         while(head1){
             ans->next=head1;
             head1=head1->next;
             ans=ans->next;
         }
         while(temp){
             ans->next=temp;
             temp=temp->next;
             ans=ans->next;
         }
         *head=head2->next;
    }
};

//{ Driver Code Starts.
int main()
{
	int test;
	cin>>test;
	while(test--)
	{
	    struct Node* head = NULL;
	    struct Node* tail = NULL;
	    int n, k;
	    cin>>n;
	    for(int i=0; i<n ;i++){
	        cin>>k;
	        append(&head, &tail, k);
	    }
	    Solution ob;
	    ob.sort(&head);
	    printList(head);
	}
	return 0;
}

// } Driver Code Ends
