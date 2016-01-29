# Populating Next Right Pointers in Each Node

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
          self.val = x
          self.left = None
          self.right = None
          self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
     def connect(self, root):
          if root :
               next_node=root.next
               left=root.left
               right=root.right
               
               if left and right:
                    left.next=right
                    #self.connect(left) #can not put "self.connect(left)" here;(right.next has not bing connected)
               if right and next_node :
                    right.next=next_node.left
                    #self.connect(right) #can not put "self.connect(right)" here
               
               self.connect(left)
               self.connect(right)
                           
        
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
     s.connect(x)
     print("")
