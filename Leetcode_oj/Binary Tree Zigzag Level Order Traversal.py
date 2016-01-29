# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        res=[]
        nodes=[]
        nodes.append(root)
        order=1
        while(nodes!=[]):
            level=[]
            for i in range(len(nodes)):
                if nodes[i]!=None:
                    level.append(nodes[i].val)
            if level!=[]:
                if order==1:
                    res.append(level)
                else:
                    antitone_level=[]
                    for j in range(len(level)):
                        antitone_level.append(level[len(level)-1-j])
                    res.append(antitone_level)
                order=order*(-1)
            temp=[]
            for i in range(len(nodes)):
                if nodes[i]!=None:
                    temp.append(nodes[i].left)
                    temp.append(nodes[i].right)
            nodes=temp
        print(res)
        return res

if __name__ == '__main__':
	root=TreeNode(3)
	l=TreeNode(9)
	r=TreeNode(20)
	rl=TreeNode(15)
	rr=TreeNode(7)
	root.left=l
	root.right=r
	r.left=rl
	r.right=rr



	s=Solution()
	s.zigzagLevelOrder(root)

