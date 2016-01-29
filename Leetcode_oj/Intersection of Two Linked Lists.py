# Intersection of Two Linked Lists

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
    	len_A=0
    	len_B=0
    	a=headA
    	b=headB
    	while a:
    		a=a.next
    		len_A=len_A+1
    	while b:
    		b=b.next
    		len_B=len_B+1
    	d=len_A-len_b
    	if d>=0:
    		for i in range(d):
    			headA=headA.next
    		while headA and headB:
    			if headA==headB:
    				return headA
    			else:
    				headA=headA.next
    				headB=headB.next
    	else:
    		for i in range(-d):
    			headB=headB.next
    		while headA and headB:
    			if headA==headB:
    				return headA
    			else:
    				headA=headA.next
    				headB=headB.next
    	return headA

