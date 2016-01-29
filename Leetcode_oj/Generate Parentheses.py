
#coding=utf-8
'''http://www.cnblogs.com/iois/p/3939612.html
'''
class Solution:
    # @param an integer
    # @return a list of string
    #def generateParenthesis(self, n):   # wrong : n==4 , '(())(())'
        #dp=[]
        #for i in range(n):
            #temp=[]
            #if i==0:
                #dp.append('()')
            #else:
                #for j in dp:
                    #temp.append(j+'()')
                    #temp.append('('+j+')')
                    #temp.append('()'+j)
                #dp=temp
                #k=len(dp)-1
                #while k>=0:
                    #for l in range(k-1):
                        #if dp[k]==dp[l]:
                            #del dp[k]
                            #k-=1
                            #break
                    #k-=1
        #return dp
    def generateParenthesis(self, n): 
        dp=[] #dp[i]用于存放出现i+1的个括号的情况
        for i in range(n):
            temp=[]
            if i==0:
                dp.append(['()'])
            else:
                for k in range(i):
                    for m in dp[k]:        # 出现k个括号的情况
                        for n in dp[i-k-1]:# 出现i-k个括号的情况
                            temp.append(m+n) # 合并
                for o in dp[i-1]:
                    temp.append('('+o+')')
                dp.append(self.delRepetition(temp))
        return dp[i]

    def delRepetition(self,A):
        # A : list
        k=len(A)-1
        while k>0:
            for l in range(k):
                if A[k] == A[l]: # A[k]A[i]重复(k>i)
                    del A[k]     # 删除
                    break        # 跳出，一次循环最大多删除一个
            k-=1
        return A

if __name__=='__main__':
    s=Solution()
    print(s.delRepetition([1,1,1,2,2,2,3,3,5]))
    print(s.generateParenthesis(4))
