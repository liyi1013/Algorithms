/* Binary Tree Right Side View
 * main.cpp-eclipse CDT
 *
 *  Created on: May 11, 2015
 *      Author: liyi
 */

#include<vector>
#include<iostream>
#include<utility>
using namespace std;

/*Definition for a binary tree node.*/
struct TreeNode {
	int val;
	TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> rightSideView(TreeNode* root)
	{
    	vector<int> res;
    	if(root){
    		//res.push_back(root->val);
    		f(root,0,res);
    	}
    	else{
    		return res;
    	}
    	return res;
    }
    void f(TreeNode* root,int level,vector<int> &res)
    {
    	if(root)
    	{
    		if(res.size()>level)
    		{
    			f(root->right,level+1,res);
    			f(root->left,level+1,res);
    		}
    		else
    		{
    			res.push_back(root->val);
    			f(root->right,level+1,res);
    			f(root->left,level+1,res);
    		}
    	}
    	else
    	{
    	}
    }
};

int main(){
	Solution s;
	TreeNode r(0);
	TreeNode l0(1);
	TreeNode r0(2);
	TreeNode l1(3);
	TreeNode r1(4);
	r.left=&l0;
	r.right=&r0;
	l0.left=&l1;
	l0.right=&r1;

	vector<int> res=s.rightSideView(&r);
	for(int i=0;i<res.size();++i){
		cout<<res[i]<<" ";
	}
return 1;
}
