class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        len_a=len(a)
        len_b=len(b)
        if len_a>len_b:
        	for i in range(len_a-len_b):
        		b='0'+b
        	len_b=len_a
        else:
        	for i in range(len_b-len_a):
        		a='0'+a
        	len_a=len_b

        res=""
        carry='0'

        for i in range(len_a):
            sum=self.addsimgleBinary(a[len_a-i-1],b[len_b-i-1],carry)
            if sum=='3':
                res='1'+res
                carry='1'
                continue
            if sum=='2':
                res='0'+res
                carry='1'
                continue
            else:
                res=sum+res
                carry='0'
                continue
        if carry=='1':
        	res='1'+res
        return res


    def addsimgleBinary(self,x,y,carry):
    	if carry=='1':
    		if x=='1' and y=='1':
    			return '3'
    		if x=='0' and y=='0':
    			return '1'
    		else:
    			return '2'
    	if carry=='0':
    		if x=='1' and y=='1':
    			return '2'
    		if x=='0' and y=='0':
    			return '0'
    		else:
    			return '1'

if __name__ == '__main__':
	s=Solution()
	print(s.addBinary("111","110"))