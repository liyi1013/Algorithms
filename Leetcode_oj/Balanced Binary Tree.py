# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
          self.val = x
          self.left = None
          self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
     def isBalanced(self, root):
          if(root==None):
               return True
          else:
               l_depth=self.__depth(root.left)
               r_depth=self.__depth(root.right)
               
               if l_depth - r_depth > 1 or r_depth - l_depth > 1:
                    return False
               else:
                    return self.isBalanced(root.left) and self.isBalanced(root.right)
     def __depth(self,root):
          if root==None:
               return 0
          else :
               l_depth=self.__depth(root.left)
               r_depth=self.__depth(root.right)
               return (l_depth+1 if l_depth>r_depth else r_depth+1)
          

if __name__=='__main__':
     x=TreeNode(0)
     y=TreeNode(1)
     z=TreeNode(2)
     z1=TreeNode(3)
     z11=TreeNode(4)
     x.left=y
     x.right=z
     z.right=z1
     z1.right=z11
     
     s=Solution()
     #s.__depth(x)
     #print(s.__depth(x))
     print(s.isBalanced(x))