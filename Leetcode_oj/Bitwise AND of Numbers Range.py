class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n): ##error
    	n_2=n
    	d_up=0
    	while n_2>=2:
    		n_2=n_2//2
    		d_up+=1
    	print d_up

    	if m<2**(d_up-1) :
    		print 2**d_up
    		return 2**d_up
    	else:
    		res=n
    		for i in range(m,n):
    			print res
    			res=res&i
    		return res
    def rangeBitwiseAnd_0(self, m, n):
        res=n
        while n>m:
            res=res&(n-1)
            n=n-1
        print res
        return res
    def rangeBitwiseAnd_1(self, m, n):
        res=n
        while res>m:
            res=res&(n-1)
        print res
        return res
    def rangeBitwiseAnd_2(self, m, n):
        i=0
        while n!=m:
            n=n>>1;
            m=m>>1;
            i=i+1;
        print n<<i;
        return n<<i;




if __name__ == '__main__':
	s=Solution()
	print s.rangeBitwiseAnd_2(5,7)
    #print s.rangeBitwiseAnd_2(3,5)