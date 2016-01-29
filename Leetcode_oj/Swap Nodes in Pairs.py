# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head==None or head.next==None:
            return head
        next_node=head.next
        temp=next_node.next
        next_node.next=head
        head.next=self.swapPairs(temp)
        return next_node
if __name__=='__main__':
    
    s=[]
    print(len(s))
    
    x=ListNode(1)
    y=ListNode(2)
    z=ListNode(3)
    x.next=y
    y.next=z
    
    ss=Solution()
    h=ss.swapPairs(x)
    print(h.val)
    hh=h.next
    print(hh.val)
    
    