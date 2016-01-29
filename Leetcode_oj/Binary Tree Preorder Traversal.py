# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root==None :
            return []
        else:
            left_order=self.preorderTraversal(root.left)
            right_order=self.preorderTraversal(root.right)
            inorder=[root.val]
            inorder=inorder+left_order+right_order
            return inorder

if __name__=='__main__':
    
    s=Solution()
    
    x=TreeNode(1)
    y=TreeNode(2)
    z=TreeNode(3)
    x.right=y
    y.left=z
    
    print(s.preorderTraversal(x))
    
    a=[1,2,3]
    b=[4,5,6]
    print(a+b)