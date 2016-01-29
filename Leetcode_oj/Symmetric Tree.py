'''2014-8-25,LY'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root==None:
            return True
        else :
            left=root.left
            right=root.right
            if(left and right and left.val==right.val):
                root1=TreeNode(0)
                root1.left=left.left
                root1.right=right.right
                root2=TreeNode(0)
                root2.left=left.right
                root2.right=right.left 
                return self.isSymmetric(root1) and self.isSymmetric(root2)
            elif(left==None and right==None):
                return True
            else :
                return False 
            
if __name__=='__main__':
    root=TreeNode(1)
    l=TreeNode(2)
    r=TreeNode(2)
    ll=TreeNode(3)
    lr=TreeNode(4)
    rl=TreeNode(4)
    rr=TreeNode(5)
    #root.left=l
    #root.right=r
    l.left=ll
    l.right=lr
    r.left=rl
    r.right=rr
    
    s=Solution()
    print(s.isSymmetric(root))