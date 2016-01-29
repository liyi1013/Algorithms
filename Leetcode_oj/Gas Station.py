class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost): # can't be accepted
        additional_gas=[]
        for i in range(len(gas)):
        	additional_gas.append(gas[i]-cost[i])
        
        list2=[]
        for i in additional_gas:
        	list2.append(i)

        additional_gas=additional_gas+list2

        for i in range(len(list2)):
        	dtank=additional_gas[i]
        	if dtank<0:
        		continue
        	for j in range(len(list2)):
        		dtank=dtank+additional_gas[i+j]
        		if dtank<0:
        			break
        	if dtank>=0:
        		return i
        return -1

    def canCompleteCircuit2(self, gas, cost): #accepted
    	additional_gas=[]
    	for i in range(len(gas)):
    		additional_gas.append(gas[i]-cost[i])
    	if sum(additional_gas)<0:
    		return -1
        start=0
        need=0
        save=0
        for i in range(len(gas)):
    		#if (additional_gas[i]>=0 and additional_gas[i-1]<0):
    		#	start=i
            if additional_gas[i]>0 and additional_gas[i]>additional_gas[save]:
                save=i
            if additional_gas[i]<0 and additional_gas[i]<additional_gas[need]:
                need=i
        if -additional_gas[need]>additional_gas[save]:
            if need==len(gas)-1:
                return 0
            else:
                return need+1
        else:
            return save
    	#return start

if __name__ == '__main__':
	s=Solution()
	gas=[3897,3898]
	cost=[3898,3897]
	print(s.canCompleteCircuit2([6,1,2,3,2,1,8],[1,7,2,2,2,8,1]))