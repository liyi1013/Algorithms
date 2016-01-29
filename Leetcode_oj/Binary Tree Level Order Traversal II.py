# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root=TreeNode(0)):
    	res=[]
    	if root is None:
    		return []
    	res_l=self.levelOrderBottom(root.left)
    	res_r=self.levelOrderBottom(root.right)
    	depth_l=len(res_l)
    	depth_r=len(res_r)
    	min_depth=min(depth_l,depth_r)
    	if depth_l>depth_r:
    		d=depth_l-depth_r
    		for i in xrange(0,d):
    			res.append(res_l[i])
    		for i in xrange(depth_r):
    			res.append(res_l[i+d]+res_r[i])
    	else:
    		d=depth_r-depth_l
    		for i in xrange(0,d):
    			res.append(res_r[i])
    		for i in xrange(depth_l):
    			res.append(res_l[i]+res_r[i+d])
    	res.append([root.val])
    	print res
    	return res
    	
if __name__ == '__main__':
	s=Solution()
	r=TreeNode(3)
	r.left=TreeNode(9)
	r.left.left=TreeNode(1)
	r.right=TreeNode(20)
	r.right.left=TreeNode(15)
	r.right.right=TreeNode(7)
	print s.levelOrderBottom(r)