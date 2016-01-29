#coding=utf-8
# Definition for singly-linked list.
class ListNode:
        def __init__(self, x):
                self.val = x
                self.next = None

class Solution:

        # 先全部加载到数组里面，然后排序，再转化成链表
        # @param two ListNodes
        # @return a ListNode
        def mergeTwoLists(self, l1, l2):
                ll=[]
                while l1:
                        ll.append(l1.val)
                        l1=l1.next
                while l2:
                        ll.append(l2.val)
                        l2=l2.next
                ll.sort()
                if(ll):
                        s=ListNode(ll[0])
                else:
                        s=None
                currentNode=s
                for i in ll[1:]:
                        temp=ListNode(i)
                        currentNode.next=temp
                        currentNode=temp
                        #print (temp.val)
                return s

        # 对指针操作
        def mergeTwoLists_1(self, l1, l2):
                if l1==None and l2: return l2
                if l2==None and l1: return l1
                if l1==None and l2==None: return None

                if l1.val<l2.val:
                        h,h1,h2=l1,l1,l2
                else:
                        h,h1,h2=l2,l2,l1
                while h1.next and h2:
                        if h1.next.val>h2.val:
                                temp=h1.next
                                h1.next=h2
                                h2=temp
                                h1=h1.next
                        else:
                                h1=h1.next
                if h2:
                        h1.next=h2
                return h

if __name__=='__main__':
        x1=ListNode(1)
        y1=ListNode(2)
        x1.next=y1 
        
        x2=ListNode(3)
        y2=ListNode(4)
        x2.next=y2
        
        s=Solution()
        #S=s.mergeTwoLists({},{})
        S=s.mergeTwoLists_1(None,None)
        
        while S:
                print(S.val)
                S=S.next
            