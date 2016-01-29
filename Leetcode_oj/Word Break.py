'''
 Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given  s = "leetcode", dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code". 
'''
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak_0(self, s, wordDict):
    #recursion -> error: "aaaaaaa",["aaaa","aaa"]
        if s=="":
            return True
        for i in range(len(s)+1):
            print s[0:i]
            if s[0:i] in wordDict:
                return self.wordBreak_0(s[i:len(s)+1], wordDict)
        return False
    def wordBreak(self, s, wordDict):#DP Accept
        s_len=len(s)
        DP=[False]*(s_len+1)
        DP[0]=True
        for i in range(s_len+1):
            for j in range(i):
                print s[j:i]
                if(s[j:i] in wordDict and DP[j]): #!! 2 condition
                    DP[i]=True
        print DP
        return DP[s_len]


if __name__=="__main__":
    s=Solution()
    word="daaaaaa"
    print word[7:7]
    d=set(["da","daa","aaaa"])
    print s.wordBreak(word,d)
    
    