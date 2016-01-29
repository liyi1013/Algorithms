class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        if target<candidates[0]:
            return []
        num_items=len(candidates)
        res=[]
        for i in range(num_items):
            if candidates[i]>target:
                break
            if candidates[i]==target:
                res.append( [candidates[i]] )
                break
            #print "candidates:",candidates[i:num_items],"target: ",target-candidates[i]
            temp=self.combinationSum(candidates[i:num_items],target-candidates[i])
            print "temp",temp,"target:",target-candidates[i]
            for j in temp:
                j.append(candidates[i])
                j.sort()# ...
                res.append(j)
        print res
        return res

if __name__ == '__main__':
    s=Solution()
    #s.combinationSum([2,3,6,7],7)
    print(s.combinationSum([2,3,6,7],8))

    c=[0,1,2,3,4,5]
    print(c[1:5])


