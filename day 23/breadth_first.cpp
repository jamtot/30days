#include <iostream>
#include <cstddef>
#include <queue>
#include <string>
#include <cstdlib>

using namespace std;	
class Node{
    public:
        int data;
        Node *left,*right;
        Node(int d){
            data=d;
            left=right=NULL;
        }
};
class Solution{
    public:
  		Node* insert(Node* root, int data){
            if(root==NULL){
                return new Node(data);
            }
            else{
                Node* cur;
                if(data<=root->data){
                    cur=insert(root->left,data);
                    root->left=cur;
                }
                else{
                   cur=insert(root->right,data);
                   root->right=cur;
                 }           
           return root;
           }
        }

	void levelOrder(Node * root)
    {
        if (root == NULL)
            return;

        queue<Node *> myQ;

        myQ.push(root);

        while (myQ.empty() == false) 
        { 
            // Print front of queue and remove it from queue 
            Node *node = myQ.front(); 
            cout << node->data << " "; 
            myQ.pop(); 
    
            /* Enqueue left child */
            if (node->left != NULL) 
                myQ.push(node->left); 
    
            /*Enqueue right child */
            if (node->right != NULL) 
                myQ.push(node->right); 
        } 
	}

};//End of Solution
int main(){
    Solution myTree;
    Node* root=NULL;
    int T,data;
    cin>>T;
    while(T-->0){
        cin>>data;
        root= myTree.insert(root,data);
    }
    myTree.levelOrder(root);
    return 0;
}
