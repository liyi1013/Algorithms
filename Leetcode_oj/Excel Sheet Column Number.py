class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
    	d=dict([('A', 1), ('B', 2), ('C', 3),('D',4),('E',5),('F',6),('G',7),('H',8),('I',9),('J',10),('K',11),('L',12),('M',13),('N',14),('O',15),('P',16),('Q',17),('R',18),('S',19),('T',20),('U',21),('V',22),('W',23),('X',24),('Y',25),('Z',26)]);
    	res=0
    	num_char=len(s)
    	for i in range(len(s)):
    		res=res+d[s[i]]*pow(26,(num_char-i-1))
    	print(res)
    	return res

s=Solution()
s.titleToNumber("ZZZ")

# "AAA" 703=
# "ZZ" 702= 26*26+26