# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        less_list=[]
        greater_list=[]
        less_node_list=ListNode(0)
        greater_node_list=ListNode(0)
        head1=less_node_list
        head2=greater_node_list
        while head!=None:
        	if head.val<x:
        		less_list.append(head.val)
        		head1.next=ListNode(head.val)
        		head1=head1.next
        	else:
        		greater_list.append(head.val)
        		head2.next=ListNode(head.val)
        		head2=head2.next
        	head=head.next
        head1.next=greater_node_list.next
        #head0=less_node_list.next
        #i=0
        #while head0!=None:
        #	print(head0.val)
        #	head0=head0.next
        #	i=i+1
        #	if i>10:
        #		break
        return less_node_list.next

        #print("less: ",less_list)
        #print("greater_list: ",greater_list)

if __name__ == '__main__':
	s=Solution()

	l1=ListNode(1)
	l2=ListNode(4)
	l3=ListNode(3)
	l4=ListNode(2)
	l5=ListNode(5)
	l6=ListNode(2)
	l1.next=l2
	l2.next=l3
	l3.next=l4
	l4.next=l5
	l5.next=l6

	s.partition(l1,3)


