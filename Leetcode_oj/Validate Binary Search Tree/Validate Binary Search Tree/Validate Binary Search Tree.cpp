#include<iostream>
#include<stdlib.h>
using namespace std;
/* Definition for binary tree*/
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
	bool isValidBST(TreeNode *root);
};

bool Solution::isValidBST(TreeNode *root)
{
	if (root == NULL) return true;
	else
	{
		if ((root->left == NULL) && (root->right == NULL))
			return true;

		if ((root->left == NULL) && (root->right != NULL) && (root->right->val > root->val))
			return isValidBST(root->right);

		if ((root->right == NULL) && (root->left != NULL) && (root->left->val < root->val))
			return isValidBST(root->left);

		if ((root->right != NULL) && (root->left != NULL) && (root->right->val > root->val) && (root->left->val < root->val))
			return (isValidBST(root->left) && isValidBST(root->right));

		else
			return false;
	}
}

int main()
{
	Solution s;
	TreeNode n(1),l(1);
	n.left = &l;
	bool b=s.isValidBST(&n);
	cout << b << endl;

}