#include<iostream>
using namespace std;

/** Definition for binary tree */
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

class BSTIterator {
public:

	TreeNode *min;
	TreeNode *next_min;

	BSTIterator(TreeNode *root) :min(NULL){
		if (root != NULL){
			min = root;
			while (min->left != NULL){
				next_min = min;
				min = min->left;
			}
		}
	}

	/** @return whether we have a next smallest number */
	bool hasNext() {
		if (next_min != NULL){
			return true;
		}
		else{
			return false;
		}
	}

	/** @return the next smallest number */
	int next() {
		if (next_min != NULL){
			return next_min->val;
		}
		else{
			return 0;
		}
	}
};

/**
* Your BSTIterator will be called like this:
* BSTIterator i = BSTIterator(root);
* while (i.hasNext()) cout << i.next();
*/