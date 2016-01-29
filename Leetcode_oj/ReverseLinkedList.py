# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
    	if head!=None:
    		list1=head
    		list2=None
    		while list1:
    			list1,list2=self.move1(list1,list2)
    		return list2
    def move1(self,list1,list2):
    	if list1!=None:
    		head=list1
    		list1=list1.next
    		head.next=list2
    		list2=head
    		return list1,list2
    def f(self, head):
    	head=head.next
    	head.val=44

if __name__ == '__main__':
	n1=ListNode(1)
	n2=ListNode(22)
	n3=ListNode(3)
	n1.next=n2
	n2.next=n3
	s=Solution()
	relist=s.reverseList(n1)
	while relist!=None:
		print(relist.val)
		relist=relist.next

#python 中参数为传引用，相当于起一个别名/指针？

#递归方法：还没写