# https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/
# 2014-8-13 - LY

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if(head==None):
            return 
        elif(head.next==None):
            return head
        current_node=head
        next_node=head.next
        while(next_node):
            if(current_node.val==next_node.val):
                current_node.next=next_node.next
                next_node=next_node.next
            else:
                current_node=next_node
                next_node=next_node.next
        return head
if __name__=="__main__":
    x=ListNode(1)
    y=ListNode(2)
    z=ListNode(1)
    z1=ListNode(2)
    x.next=z
    z.next=y
    y.next=z1
    
    s=Solution()
    h=s.deleteDuplicates(x)
    while(h!=None):
        print(h.val)
        h=h.next
        