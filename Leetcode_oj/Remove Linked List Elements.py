# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
		if head==None:
			return head
		else:
			head_before=ListNode(0)
			head_before.next=head
			currrent_node=head_before
			#while currrent_node and currrent_node.next and currrent_node.next.val==val:
			#	currrent_node.next=currrent_node.next.next
			while currrent_node and currrent_node.next:
				if currrent_node.next.val==val:
					currrent_node.next=currrent_node.next.next
				else:#here is a Traps(must have else:)
					currrent_node=currrent_node.next
			return head_before.next

if __name__ == '__main__':
	l=ListNode(1)
	l.next=ListNode(1)
	l.next.next=ListNode(2)
	l.next.next.next=ListNode(1)
	l.next.next.next.next=ListNode(6)
	s=Solution()

	r=s.removeElements(l,1)

	while r:
		print r.val
		r=r.next