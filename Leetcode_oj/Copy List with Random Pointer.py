'''
liyi 2015-5-22
'''
# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        head_2=head
        head_3=head
        d=dict();
        before=RandomListNode(0)
        h=before
        while head_2!=None:
            new_node=RandomListNode(head_2.label)
            before.next=new_node
            before=before.next
            d[head_2.label]=new_node
            head_2=head_2.next
        h_2=h.next
        h_3=h.next
        while head_3!=None:
            if head_3.random and head_3.random.label in d:
                h_2.random=d[head_3.random.label]
            h_2=h_2.next
            head_3=head_3.next
        return h_3

s=Solution()

r1=RandomListNode(1)
r2=RandomListNode(2)
r3=RandomListNode(3)
r4=RandomListNode(4)
r1.next=r2
r2.next=r3
r3.next=r4
r1.random=r3
r2.random=r4

r=s.copyRandomList(r1)
while r:
    if r.random:
        print r.label," ",r.random.label
    else:
        print r.label
    r=r.next