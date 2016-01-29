# Word Ladder II 
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        res=self.findLadders_n(start, end, dict)
        return len(res)
    
    def findLadders_n(self, start, end, dict):
        if start==end :
            return [start]
        if dict==[]:
            return []
        else:
            ss=self.findCandidate(start, dict)
            ee=self.findCandidate(end, dict)
            if (ss==ee):
                print(start,'->',ss,'->',end)
                return [start]+[ss]+[end]
            print (start,'->',ss)
            self.delString(ss, dict)
            res=self.findLadders_n(ss, end, dict)
            return [start]+res
    
    def findCandidate(self,str,dict):
        # return a lost of strings
        n=len(str)
        if dict==[] or dict==None:
            return []
        result=''
        for i in dict:
            for j in range(n):
                str_t=str[0:j]+str[j+1:n] 
                i_t=i[0:j]+i[j+1:n] 
                if str_t==i_t and str[j]!=i[j] :
                    #result.append(i)
                    result=i
        return result
    
    def delString(self,str,dict):
        n=len(dict)
        for i in range(n):
            if str==dict[i]:
                del dict[i]
                return #dict
    

if __name__=='__main__':
    
    str='hit'
    d=["hot","hit","cog","dot","dog"]
    s=Solution() 
    
    #print(str,'->',s.findCandidate(str, d))
    #s.delString('hot',d)
    #print(s.findCandidate('hot', d),len(d))
    
    #s.delString('dot',d)
    #print(d,len(d))    
    res=s.findLadders(str, 'cog', d)
    print(res)
    
    #str1=str[0:1]+str[2:3]
    #d2=d
    #d2[1]='l'
    #del str[1] # str: string ,'str' object doesn't support item deletion
    print(d)
    
    #dd=[]
    #for ss in [dd]:
        #print(ss)
        
   # print(type(d))