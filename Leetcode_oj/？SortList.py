# time O(nlog(n))
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
    	if head is not None:
        	self.quicksort(head,None)
        return head

    def quicksort(self,node_head,node_end):
    	if node_head is not node_end :
            q=self.patition(node_head,node_end)
            self.quicksort(node_head,q)
            self.quicksort(q.next,node_end)
    def patition(self,head,end):
        #@return{ListNode}
    	if head is None:
    		return None
    	else:
    		i=head
    		j=head.next
    		x=head.val
    		while j is not end:
    			if j.val<x:
    				self.ListNode_Val_Swap(i,j)
    				i=i.next
    			j=j.next
    		i.val=x
    		return i

    # swap 2 ListNodes' val
    def ListNode_Val_Swap(self,node1,node2):
    	node1.val,node2.val=node2.val,node1.val
if __name__ == '__main__':
	s=Solution()
	l=l1=ListNode(6)
	l1.next=ListNode(3)
	l1.next.next=ListNode(0)
	for x in range(896):
		l1.next=ListNode((100-x)%9)
		l1=l1.next

	#l=ListNode(1)
	s.sortList(l)
	while l:
		print l.val
		l=l.next

'''
	ll1=ListNode(22);
	ll2=ListNode(33);
	s.ListNode_Val_Swap(ll1,ll2)
	print(ll1.val)
	print(ll2.val)
'''