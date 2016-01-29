# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

#my_lists.sort(cmp=lambda x,y:cmp(x.val,y.val))
class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists_0(self, lists):
        lists = [list for list in lists if list is not None]
        if len(lists)<=0:
            return lists
        l=lists[0]
        for i in range(1,len(lists)):
            l=self.merge2lists(l,lists[i])
        return l

    def mergeKLists(self, lists):
        lists = [list for list in lists if list is not None]
    	if len(lists)<=0:
    		return lists
    	if len(lists)==1:
    		return lists[0]
    	d=[]
    	l=lists[0]
    	for i in range(0,len(lists)-1,2):
    		l=self.merge2lists(lists[i],lists[i+1])
    		d.append(l)
    	if len(lists)%2==1:
    		d.append(lists[len(lists)-1])
    	return self.mergeKLists(d)

    def merge2lists(self,list_1,list_2):
    	if list_1 is None:
    		return list_2
    	if list_2 is None:
    		return list_1
    	if list_1.val>=list_2.val:
    		head_1=list_1      #big
    		head=head_2=list_2 #small
    	else:
    		head_1=list_2      #big
    		head=head_2=list_1 #small
    	while head_2.next!=None:
    		if head_2.next.val>head_1.val:
    			head_2.next,head_1=head_1,head_2.next
    		head_2=head_2.next
    	if head_1!=next:
    		head_2.next=head_1
    	return head
    		
if __name__ == '__main__':
	s=Solution()
	l1=ListNode(-1)
	l1.next=ListNode(1)

	l2=ListNode(-1)
	l2.next=ListNode(1)
	l2.next.next=ListNode(4)
	
	l3=ListNode(-1)
	l3.next=ListNode(0)
	l3.next.next=ListNode(1)
	l3.next.next.next=ListNode(2)
	
	ls=[l1,l2,l3]

	l=s.mergeKLists_0(ls)
	while l!=None:
		print l.val
		l=l.next




        