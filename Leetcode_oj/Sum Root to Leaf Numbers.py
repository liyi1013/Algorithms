# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    #def sumNumbers(self, root):   ### 错误
        #if root==None:
            #return 0
        #else:
            #root_l=0
            #root_r=0
            #rootVal=0
            #if root.left:
                #l_sum=self.sumNumbers(root.left)
                #n=self.__digits__(l_sum)
                #root_l=root.val*10**n+l_sum
                #print(root_l)
            #if root.right:
                #r_sum=self.sumNumbers(root.right)
                #n=self.__digits__(r_sum)
                #root_r=root.val*10**n+r_sum
                #print(root_r)
            #if root.left is None and root.right is None :
                #rootVal=root.val
                #print(root.val)
            
            #print(root_l+root_r+rootVal)
            #return root_l+root_r+rootVal
        
    #def __digits__(self,num):
        #if num==0:
            #return 1
        #else:
            #n=0
            #while num>0:
                #num=num//10
                #n+=1
            #return n
    def sumNumbers(self, root):
        if root is None:
            return 0
        else:
            return self.sumNumbers1(root,0)
    def sumNumbers1(self, root,num):
        root_l=0
        root_r=0
        rootVal=0
        if root.left:
            root_l=self.sumNumbers1(root.left,num*10+root.val)
            print(root_l)
        if root.right:
            root_r=self.sumNumbers1(root.right,num*10+root.val)
            print(root_r)
        if root.left is None and root.right is None :
            print(num*10+root.val)
            return num*10+root.val
        else:
            return root_l+root_r

if __name__=='__main__':
    s=Solution()
    
    r=TreeNode(8)
    
    x=TreeNode(3)
    y=TreeNode(5)
    
    z=TreeNode(9)
    zl=TreeNode(9)
    zr=TreeNode(5)
    
    #z.left=zl
    #z.right=zr
    
    #x.right=z
    #r.left=x
    #r.right=y
    
    print(s.sumNumbers(r))
'''应该从上向下递归，而不是重下向上递归'''