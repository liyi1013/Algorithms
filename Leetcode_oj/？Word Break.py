class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        for i in range(len(s)):
            if s[i] in dict:
                return self.wordBreak(s[i+1,len(s)], dict)
        else
            
        pass

if __name__=="__main__":
    t=set(['aa','b','c','c'])
    print(t)
    c=[i for i in t]
    print(c)