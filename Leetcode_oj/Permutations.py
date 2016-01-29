class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        length=len(num)
        if length==1:
            return [num]
        else:
            res=[]
            for i in range(length):
                d=self.permute(num[0:i]+num[i+1:length])
                for j in d:
                    res.append(j+[num[i]])
            #È¥³ýÖØ¸´Ïî
            k=len(res)-1
            while k>0:
                for j in range(k):
                    if self.IsSameList(res[j], res[k]):
                        del res[k]
                        break
                k-=1   
            return res
        
    def IsSameList(self,A,B):
        an=len(A)
        bn=len(B)
        if (an!=bn):
            return False
        else:
            for i in range(an):
                if (A[i]!=B[i]):
                    return False
            return True
         
if __name__=='__main__':
    num=[1,2,3]
    s=Solution()
    print(s.permute([1,1,3]))