class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        num_items=len(A)
        if num_items==0:
        	return [-1,-1]
        head=0
        end=num_items  #?
        mid=int((head+end)/2)
        while A[mid]!=target:
        	if end-head<2 :
        		return [-1,-1]
        	if A[mid]<target:
        		head=mid
        	elif A[mid]>target:
        		end=mid
        	mid=int((head+end)/2)
        print(head,mid,end)

        head_begin=head
        head_end=mid
        head_mid=int((head_begin+head_end)/2)
        end_begin=mid
        end_end=end
        end_mid=int((end_begin+end_end)/2)

        while head_end-head_begin>1:
        	if A[head_mid]<target:
        		head_begin=head_mid
        	elif A[head_mid]==target:
        		head_end=head_mid
        	head_mid=int((head_begin+head_end)/2)
        	print("head ",head_begin,head_mid,head_end)
        if A[head_begin]==target: #.. 
        	head=head_begin
        else:
        	head=head_end

        while end_end-end_begin>1:
        	if A[end_mid]>target:
        		end_end=end_mid
        	elif A[end_mid]==target:
        		end_begin=end_mid
        	end_mid=int((end_begin+end_end)/2)
        	print("end",end_begin,end_mid,end_end)
        end=end_begin


        return [head,end]

if __name__ == '__main__':
	s=Solution()
	A=[2,2,2,3,3]
	print(s.searchRange(A,3))


