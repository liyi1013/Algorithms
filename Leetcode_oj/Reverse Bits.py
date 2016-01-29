# given input 43261596 
# (represented in binary as 00000010100101000001111010011100), 
# return 964176192 
# (represented in binary as 00111001011110000010100101000000).
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
    	res=int(0)
    	nn=int(n)
    	for i in range(31):
    		if nn&1:
    			res=res|1
    		nn=nn>>1
    		res=res<<1
    		#print "nn:" ,bin(nn)
    		#print "res:", bin(res)
    	if nn&1:
    		res=res|1
    	return res

if __name__ == '__main__':
	s=Solution()
	n=2147483648
	r=s.reverseBits(n)
	print bin(n)
	print bin(r)
	print r


        