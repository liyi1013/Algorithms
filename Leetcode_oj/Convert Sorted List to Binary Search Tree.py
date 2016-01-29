# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
	def disp(self):
		print self.val
		if(self.left!=None):
			self.left.disp()
		if(self.right!=None):
			self.right.disp()
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
    	l=[]
    	while(head!=None):
    		l.append(head.val)
    		head=head.next
    	#print l
    	return self.sortArray2BST(l)
    def sortArray2BST(self,arr):
    	if(len(arr)==0):
    		return None
    	if(len(arr)==1):
    		treenode=TreeNode(arr[0])
    	#	print "arr[0]",arr[0]
    		return TreeNode(arr[0])
    	else:
    		mid=len(arr)/2
    	#	print ("mid",mid)
    		treenode=TreeNode(arr[mid])
    		treenode.left=self.sortArray2BST(arr[0:mid])
    		treenode.right=self.sortArray2BST(arr[mid+1:len(arr)])
    		return treenode


if __name__ == '__main__':
	s=Solution()
	l=ListNode(1)
	l1=ListNode(2)
	l2=ListNode(3)
	l3=ListNode(5)
	l.next=l1
	l1.next=l2
	l2.next=l3
	t=s.sortedListToBST(l)
	t.disp()
	#print t.right
	#d=[1,2,3,5]
	#print d[0:2]
	#print d[3:len(d)]
	#print 1/2