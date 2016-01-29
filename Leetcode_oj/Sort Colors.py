class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        A=self.insertSort(A)
        a=b=c=0
        for i in A:
            if i==0: a+=1
            if i==1: b+=1
            if i==2: c+=1
        A=[a,b,c]
        return A
    
    def insertSort(self,A):
        for j in range(1,len(A)):
            key=A[j]
            i=j-1
            while i>=0 and A[i]>key:
                A[i+1]=A[i]
                i-=1
            A[i+1]=key
        return A
    
if __name__=='__main__':
    s=Solution()
    print(s.insertSort([1,2,0,3]))
    
   # d='1234'
   # print(d[1])