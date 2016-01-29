class Solution:
    # @return an integer
    def minDistance(self, word1, word2): # Time Limit Exceeded
        lengtg_word1=len(word1)
        lengtg_word2=len(word2)
        #if lengtg_word1>=lengtg_word2:
            #max_comm=self.lcs(word1,word2)
            #return lengtg_word1-max_comm
        #else:
            #max_comm=self.lcs(word2,word1)
            #return lengtg_word2-max_comm
        if (lengtg_word1==lengtg_word1 and lengtg_word1==1 ) and (word1 is not word2):
            return 1
        max_comm=self.lcs(word2,word1)
        return lengtg_word1+lengtg_word2-2*max_comm
	
    def lcs(self,s1,s2):
        length_s1=len(s1)
        length_s2=len(s2)
        c=[]
        d=[]
        dp=[[0 for x in range(length_s2+1)]for y in range(length_s1+1)]
        for i in range(length_s1):
            for j in range(length_s2):
                if s1[i]==s2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                    c.append(i)
                    d.append(j)
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])

        print(dp[length_s1][length_s2])

        print(c)
        print(d)
        return dp[length_s1][length_s2]

if __name__ == '__main__':
	s=Solution()
	print(s.minDistance("sea","ate"))