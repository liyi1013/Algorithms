# Given a binary tree and a sum, 
# find all root-to-leaf paths where each path's sum equals the given sum. 

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
    	if (root==None):
    		return []
    	elif root.left==None and root.right==None and root.val==sum:
    		return [[root.val]]
    	else:
    		res=[]
    		res_left=self.pathSum(root.left ,sum-root.val)
    		print "res_left:",res_left
    		res_right=self.pathSum(root.right ,sum-root.val)
    		print "res_right:",res_right
    		for i in res_left:
    			temp=[root.val]+i
    			res.append(temp)
    		for i in res_right:
    			temp=[root.val]+i
    			res.append(temp)
    		return res

if __name__ == '__main__':
	'''
	r=TreeNode(5)
	r.left=TreeNode(4)
	r.left.left=TreeNode(11)
	r.left.left.left=TreeNode(7)
	r.left.left.right=TreeNode(2)
	r.right=TreeNode(8)
	r.right.left=TreeNode(13)
	r.right.right=TreeNode(4)
	r.right.right.left=TreeNode(5)
	r.right.right.right=TreeNode(1)
	'''

	r=TreeNode(-2)
	r.right=TreeNode(-3)

	s=Solution()
	res=s.pathSum(r,-6)
	print(res)