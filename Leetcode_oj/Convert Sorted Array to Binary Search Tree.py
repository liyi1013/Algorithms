# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if num==[]:
            return 
        else:
            length=len(num)
            if(length==1):
                mid_node=TreeNode(num[0])
            else:
                mid=length//2
                mid_node=TreeNode(num[mid])
                mid_node.left=self.sortedArrayToBST(num[0:mid])
                mid_node.right=self.sortedArrayToBST(num[mid+1:length])
            return mid_node            
            

if __name__=='__main__':
    
    
    #num=[1,2,3,4,5,6,7]
    #num=[1,2,3]
    num=[]
    
    
    s=Solution()
    res=s.sortedArrayToBST(num)
    #res_l=res.left
    #res_r=res.right
    print(res)#,res_l.val,res_r.val
    #length=len(num)
    #mid=length//2
    #print (length,mid,num[mid],num[0:mid],num[mid+1:length])