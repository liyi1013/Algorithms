# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
    	self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
    	num_left_nodes=self.num_nodes(root.left)
    	print num_left_nodes
        if num_left_nodes+1>k:
        	return self.kthSmallest(root.left,k)
        elif num_left_nodes+1==k:
        	return root.val
        else:
        	return self.kthSmallest(root.right,k-num_left_nodes-1)
    def num_nodes(self,root):
    	if root is None:
    		return 0
    	else:
    		return self.num_nodes(root.left)+self.num_nodes(root.right)+1
if __name__ == '__main__':
	s=Solution()
	r=TreeNode(3)
	r.left=TreeNode(2)
	r.left.left=TreeNode(1)
	r.right=TreeNode(4)

	print("k:",s.kthSmallest(r,4))