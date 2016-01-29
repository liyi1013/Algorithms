# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):  #  How to determine the boundary conditions
        if root is None : return 0
        if root.left is None and root.right is None:
            return 1
        if root.left and root.right is None:
            print('left:',self.minDepth(root.left))
            return self.minDepth(root.left)+1
        if root.right and root.left is None:
            print('right:',self.minDepth(root.right))
            return self.minDepth(root.right)+1
        else: 
            l_depth=self.minDepth(root.left)
            r_depth=self.minDepth(root.right)
        return min(l_depth,r_depth)+1
    
r=TreeNode(1)
rl=TreeNode(1)
rr=TreeNode(1)
r.left=rl
r.right=rr

x=TreeNode(1)
y=TreeNode(1)
rl.left=x
#rr.right=y


s=Solution()
print (s.minDepth(r))
        