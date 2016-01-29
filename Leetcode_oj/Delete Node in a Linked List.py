# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
    	head=node
    	while head.next.next is not None:
    		head.val=head.next.val
    		head=head.next
    	head.val=head.next.val
    	head.next=None

        