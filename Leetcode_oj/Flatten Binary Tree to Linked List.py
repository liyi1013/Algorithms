# Given a binary tree, flatten it to a linked list in-place. 
# recursion
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root): 
    	self.f(root)
    def f(self,root):
    	if root:
    		right_node=root.right
    		root.right=self.f(root.left)
    		root.left=None # <-maybe forget!!!
    		t=root
    		while(t.right):
    			t=t.right
    		t.right=self.f(right_node)
    		return root
    	else:
    		return root

if __name__ == '__main__':
	r=TreeNode(0)
	r.left=TreeNode(2)
	r.left.left=TreeNode(3)
	r.left.right_tree=TreeNode(4)
	r.right=TreeNode(5)
	r.right.right=TreeNode(6)

	s=Solution()
	s.flatten(r)
	while r:
		print r.val
		r=r.right
