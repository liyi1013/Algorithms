'''Same Tree -- leetcode
Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

2014-8-12
author : LY '''
import sys
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if (p==None and q==None):
            return True
        elif(p and q and p.val==q.val):
            return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
        else:
            return False

if __name__=='__main__':
    y=TreeNode(5)
    y.left=TreeNode(4)
    y.right = TreeNode(6)     
    x=TreeNode(5)
    x.left=TreeNode(4)
    x.right = TreeNode(16) 
    
    s=Solution()
    
    print(s.isSameTree(x, y))

            
            
        
        