# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if(head==None or head.next==None or head.next.next==None):
            return False
        node_1=head
        node_2=head.next
        while node_1 and node_2:
            if node_1==node_2:
                return True
            else:
                node_1=node_1.next
                if node_2.next:
                    node_2=node_2.next.next
                else:
                    return False
        return False
        