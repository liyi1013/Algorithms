# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root==None :
            return False            
        if root.val==sum and root.left is None and root.right is None:
            return True
        #elif  root.val==sum:  #���ָ��������������Ͳ����ˣ���������������ˣ���������֮��Ϊ0 Ҳ����ȷ��
        #    return False
        else:
            print(root.val,sum)
            return (self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val))

if __name__=='__main__':
    s=Solution()
    
    r=TreeNode(1)
    x=TreeNode(-2)
    y=TreeNode(-3)
    zl=TreeNode(1)
    zll=TreeNode(-1)
    r.left=x
    r.right=y
    x.left=zl
    zl.left=zll
    
    
    print(s.hasPathSum(r, -1))