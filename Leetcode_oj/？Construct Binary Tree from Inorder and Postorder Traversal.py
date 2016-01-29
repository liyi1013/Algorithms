# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
    	n=len(inorder)
    	if n==0:
    		return None
    	r=TreeNode(postorder[n-1])
    	if n==1:
    		return r
    	else:
    		j=0
    		while inorder[j]!=postorder[n-1]:
    			j=j+1
    		r.left=self.buildTree(inorder[0:j],postorder[0:j])
    		if n>j+1:
    			r.right=self.buildTree(inorder[j+1:n],postorder[j:n-1])
    	return r

    def buildTree_2(self, inorder, postorder):
    	n=len(inorder)
    	if n==0:
    		return None
    	r=TreeNode(postorder[n-1])
    	if n==1:
    		return r
    	else:
    		j=inorder.index(r.val)
    		r.left=self.buildTree(inorder[0:j],postorder[0:j])
    		if n>j+1:
    			r.right=self.buildTree(inorder[j+1:n],postorder[j:n-1])
    	return r

if __name__ == '__main__':
	s=Solution()
	r=s.buildTree([],[])
	r=s.buildTree_2([1,2,3,4], [2,1,4,3])
	print r.val,r.left.val,r.right.val,r.left.right.val
        