# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
    	res=[]
    	level=[]
    	if (root):
            t=[root.val]
            level=[root]
        while(level!=[]):
            level_next=[]
            res.append(t)
            t=[]
            for i in level:
                if(i.left):
                    level_next.append(i.left)
                    t.append(i.left.val)
                if(i.right):
                    level_next.append(i.right)
                    t.append(i.right.val)
                level=level_next
    	return res

if __name__ == '__main__':
	root=TreeNode(1)
	root.left=TreeNode(2)
	root.right=TreeNode(3)
	root.left.left=TreeNode(6)
	root.left.right=TreeNode(4)
	root.right.right=TreeNode(8)
	root.right.left=TreeNode(7)
	s=Solution()
	print(s.levelOrder(root))

