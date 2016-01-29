class Solution:
    # @param num, a list of integers
    # @return an integer
    # Runtime: O(n), Space: O(n) — Hash table: Maintain a hash table of the counts of each element, then find the most common one.
    def majorityElement1(self, num):
    	d=dict()
    	for i in num:
    		if i not in d:
    			d[i]=1
    		else:
    			d[i]+=1
    	#print(d)
    	max_num=0
    	index=0
    	for i in d:
    		if (d[i]>=max_num):
    			index=i
    			max_num=d[i]
    	return index
    # Runtime: O(n log n) — Sorting
    def majorityElement2(self, num):
    	num.sort()
    	return (num[int(len(num)/2)])

s=Solution()
r=s.majorityElement2([1,1,1,1,2,3,4])
print(r)
 
