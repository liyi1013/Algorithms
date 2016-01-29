'''
Created on 2014-8-11
@author: LY
Maximum Depth of Binary Tree 
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self , root):
        if root==None:
            return 0
        else :
            Depth_r=self.maxDepth(root.right)
            Depth_l=self.maxDepth(root.left)
            if(Depth_r>=Depth_l):
                return Depth_r+1
            else:
                return Depth_l+1

if __name__ == '__main__':
    y=TreeNode(5)
    x=TreeNode(5)
    x.left=TreeNode(TreeNode(4))
    x.right = TreeNode(6)
    y.left = x
    
    s=Solution()
    sd=s.maxDepth(x)
    sy=s.maxDepth(y)
    print(sd)
    print(sy)
    s.__class__()