// Binary Tree Preorder Traversal - do with stack
#include<iostream>
#include<stack>

using namespace std;

// Definition for binary tree
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };
 
vector<int> preorderTraversal(TreeNode *root) {

    vector<int> res;
    if(root==NULL)
		return res;
	
    TreeNode* node=root;
    res.push_back(node->val); 

	stack<TreeNode*> stackNodes;

    if(node->right) // 先右子树 
        stackNodes.push(node->right);
    if(node->left) // 后左子树 
        stackNodes.push(node->left);

    while(!stackNodes.empty()){

        node = stackNodes.top();
        stackNodes.pop();

        res.push_back(node->val);

        if(node->right)
            stackNodes.push(node->right);
        if(node->left)
            stackNodes.push(node->left);
    } 
    return res;
}
