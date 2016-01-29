# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head==None:
            return 
        pre_head=ListNode(0)
        pre_head.next=head
        ruler_end=pre_head
        ruler_head=pre_head
        while n:
            ruler_end=ruler_end.next
            n-=1
            #print(n,ruler_end.val)
        while ruler_end.next!=None :
            ruler_end=ruler_end.next
            ruler_head=ruler_head.next
        temp=ruler_head.next
        ruler_head.next=temp.next
        return pre_head.next

if __name__=='__main__':
    s=Solution()
    l1=ListNode(1)
    l2=ListNode(2)
    l3=ListNode(3)
    l4=ListNode(4)
    l5=ListNode(5)
    l1.next=l2
    l2.next=l3
    l3.next=l4
    l4.next=l5
    
    head=s.removeNthFromEnd(l1, 5)
    
    while(head!=None):
        print(head.val)
        head=head.next