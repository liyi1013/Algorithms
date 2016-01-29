# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root==None :
            return []
        else:
            left_order=self.inorderTraversal(root.left)
            right_order=self.inorderTraversal(root.right)
            inorder=[root.val]
            inorder=left_order+inorder+right_order
            return inorder

if __name__=='__main__':
    
    s=Solution()
    
    x=TreeNode(1)
    y=TreeNode(2)
    z=TreeNode(3)
    x.right=y
    y.left=z
    
    print(s.inorderTraversal(x))
    
    a=[1,2,3]
    b=[4,5,6]
    print(a+b)