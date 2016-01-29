class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if len(s)==0 or s==' ':
            return 0
        l=0  #record the length of word
        p=0  #p==1: what before char i is " "
        for i in s:
            if i==' ':
                p=1
            elif p==1 and i!=" ":
                l=1
                p=0
            else:
                l+=1
        print(l)
        return l
        
s=Solution()
s.lengthOfLastWord(' hhh      add  '  )