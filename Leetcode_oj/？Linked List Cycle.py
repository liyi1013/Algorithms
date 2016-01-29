# Definition for singly-linked list.
class ListNode:
         def __init__(self, x):
                  self.val = x
                  self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
         def hasCycle(self, head=ListNode(0)):
                  if(head==None or head.next==None):
                           return False
                  current_node=head
                  next_node=head.next
                  while(current_node.next!=None):
                           if(next_node.next==current_node):
                                    return True
                           else:
                                    return self.linkToNode(next_node,current_node)      
         def linkToNode(self, y=ListNode(0) ,x=ListNode(0)):
                  #if y--->x ,return True
                  if (y.next==None):
                           return False
                  elif(y.next==x):
                           return True
                  else:
                           return self.linkToNode(y.next,x)
                           
if __name__=="__main__":
         x=ListNode(1)
         y=ListNode(2)
         z=ListNode(2)
         x.next=y
         #y.next=z
         #z.next=x
         
         s=Solution()
         print(s.hasCycle(x))