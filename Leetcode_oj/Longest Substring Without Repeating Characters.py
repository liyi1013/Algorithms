#coding=utf-8
class Solution:
    # @return an integer
    def lengthOfLongestSubstring_0(self, s): #error :"dvdf"->"vdf" 3 not 2
        hashtable=set()
        dp=[]
        for i in range(len(s)):
        	if s[i] in hashtable:
        		dp.append(1)
        		hashtable=set(s[i])
        	else:
        		if(len(dp)==0):
        			dp.append(1)
        		else:
        			dp.append(dp[i-1]+1)
        		hashtable.add(s[i])
        	#print dp
        	#print hashtable
        dp.append(0)
        print dp
        return max(dp)
    def lengthOfLongestSubstring_1(self, s): ## right but takes too mach time deal with dig data
        hashtable={}
        dp=[0]*len(s)
        i=0
        while(i<len(s)):
            if s[i] in hashtable:
                i=hashtable[s[i]]+1
                hashtable={s[i]:i}
                dp[i]=1
            else:
                dp[i]=(dp[i-1]+1)
                hashtable[s[i]]=i
            i+=1
        dp.append(0)
        print dp
        return max(dp)
    def lengthOfLongestSubstring_2(self, s): 
        hashtable={}
        begin=0;
        end=0;
        l=0;
        i=0
        while(i<len(s)):
            if s[i] in hashtable:
                i=hashtable[s[i]]+1
                hashtable={s[i]:i}
                end=i
                begin=i
            else:
                hashtable[s[i]]=i
                end=i
            print l
            l=max(l,end-begin+1)
            i+=1
        return l
    def lengthOfLongestSubstring(self, s): 
        hashtable={}
        dp=[0]*len(s)
        i=0
        while(i<len(s)):
            if s[i] in hashtable:
                dp[i]=i-hashtable[s[i]]
                hashtable[s[i]]=i
            else:
                dp[i]=(dp[i-1]+1)
                #dp[i]=len(hashtable)
                hashtable[s[i]]=i
            i+=1
            print dp
            print hashtable
        dp.append(len(hashtable))
        return max(dp)

    def lengthOfLongestSubstring_1_1(self, s): 
        hashtable={}
        dp=[0]*len(s)
        lastLongest = 0
        for i in xrange(len(s)):
            if s[i] in hashtable:
                lastOccur=hashtable[s[i]]
                if(lastLongest>=i-lastOccur):
                    lastLongest=i-lastOccur
                else:
                    lastLongest+=1
            else:
                lastLongest+=1
            hashtable[s[i]]=i
            dp[i]=lastLongest
        print dp
        return max(dp)
    def lengthOfLongestSubstring_1_2(self, s):
        hashtable={}
        res=lastLongest = 0
        for i in xrange(len(s)):
            if s[i] in hashtable:
                lastOccur=hashtable[s[i]]
                if(lastLongest>=i-lastOccur):
                    lastLongest=i-lastOccur
                else:
                    lastLongest+=1
            else:
                lastLongest+=1
            hashtable[s[i]]=i
            res=max(lastLongest,res)
        return res

if __name__ == '__main__':
    s=Solution()
    ss="abcabcff"
    print s.lengthOfLongestSubstring_1_1("eeeeeefe哈哈v")
