class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        additional_gas=[]
        for i in range(len(gas)):
            additional_gas.append(gas[i]-cost[i])
        if sum(additional_gas)<0:
            return -1
        need=0
        save=0
        for i in range(len(gas)):
            if additional_gas[i]>0 and additional_gas[i]>additional_gas[save]:
                save=i
            if additional_gas[i]<0 and additional_gas[i]<=additional_gas[need]:
                if i<len(gas)-1 and additional_gas[i+1]>0:
                    need=i
        if -additional_gas[need]>additional_gas[save]:
            #if need==len(gas)-1:
            #    return 0
            #else:
            return need+1
        else:
            return save

if __name__ == '__main__':
	s=Solution()
	gas=[3897,3898]
	cost=[3898,3897]
	print(s.canCompleteCircuit([6,1,2,3,2,1,8],[1,7,2,2,2,8,1]))