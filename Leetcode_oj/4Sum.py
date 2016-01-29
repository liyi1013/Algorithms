#coding=utf-8
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def fourSum(self, nums, target):
        n=len(nums)
        if n<4:
            return []
        res=[]
        nums=sorted(nums)

        for i in range(n-3):
            #if i>0 and nums[i] == nums[i-1]: # avoid duplication
            #    continue
            target_3=target-nums[i]
            for j in range(i+1,n-2):
                if j>0 and nums[j] == nums[j-1]: # avoid duplication
                    continue
                f=j+1
                k=n-1
                while f<k:
                    if f > j + 1 and nums[f] == nums[f-1]: # avoid duplication
                        f += 1
                        continue
                    if k < len(nums) - 1 and nums[k] == nums[k+1]: # avoid duplication
                        k -= 1
                        continue
                    sum_3=nums[j]+nums[f]+nums[k]-target_3
                    if sum_3>0:
                        k-=1
                    elif sum_3<0:
                        f+=1
                    else:
                        res.append( [nums[i] , nums[j] ,nums[f], nums[k] ] )
                        k-=1
                        f+=1
        return res

    def fourSum_1(self, nums, target):# 更好的办法
        results=set()
        res=[]
        num=sorted(nums)
        new_num=[]
        filter=dict()
        for x in num:
            if x not in filter:
                filter[x]=1
                new_num.append(x)
            elif filter[x]<=4:  # 大于4 无意义
                filter[x]+=1;
                new_num.append(x)

        pairs=[] # 所有的可能的2个数的组合 的索引
        len_new_num=len(new_num)
        for i in range(len_new_num):
            for j in range(i+1,len_new_num):
                pairs.append([i,j])

        twoSums=dict() # 所有的可能的2个数的组合的和-索引 的字典
        for pair in pairs:
            if (new_num[pair[0]]+new_num[pair[1]]) in twoSums:
                twoSums[(new_num[pair[0]]+new_num[pair[1]])].append(pair)
            else:
                twoSums[(new_num[pair[0]]+new_num[pair[1]])]=[pair]

        temp=[] # 所有的和为target的组合的索引
        for num1 in twoSums:
            num2=target-num1
            if  num2>=num1 and num2 in twoSums:
                p1=twoSums[num1]
                p2=twoSums[num2]
                for i in p1 :
                    filter[new_num[i[0]]]-=1
                    filter[new_num[i[1]]]-=1
                    for j in p2:
                        if filter[new_num[j[0]]]>0:
                            filter[new_num[j[0]]]-=1
                            if filter[new_num[j[1]]]>0:
                                t=[i[0],i[1],j[0],j[1]]
                                t=sorted(t)
                                if t not in temp:
                                    temp.append(t)
                            filter[new_num[j[0]]]+=1
                    filter[new_num[i[0]]]+=1
                    filter[new_num[i[1]]]+=1

        for i in temp:
            d=[new_num[i[0]],new_num[i[1]],new_num[i[2]],new_num[i[3]]]
            if d not in res:
                res.append(d)
        return res

if __name__ == '__main__':
    s=Solution()
    #p=[91277418,66271374,38763793,4092006,11415077,60468277,1122637,72398035,-62267800,22082642,60359529,-16540633,92671879,-64462734,-55855043,-40899846,88007957,-57387813,-49552230,-96789394,18318594,-3246760,-44346548,-21370279,42493875,25185969,83216261,-70078020,-53687927,-76072023,-65863359,-61708176,-29175835,85675811,-80575807,-92211746,44755622,-23368379,23619674,-749263,-40707953,-68966953,72694581,-52328726,-78618474,40958224,-2921736,-55902268,-74278762,63342010,29076029,58781716,56045007,-67966567,-79405127,-45778231,-47167435,1586413,-58822903,-51277270,87348634,-86955956,-47418266,74884315,-36952674,-29067969,-98812826,-44893101,-22516153,-34522513,34091871,-79583480,47562301,6154068,87601405,-48859327,-2183204,17736781,31189878,-23814871,-35880166,39204002,93248899,-42067196,-49473145,-75235452,-61923200,64824322,-88505198,20903451,-80926102,56089387,-58094433,37743524,-71480010,-14975982,19473982,47085913,-90793462,-33520678,70775566,-76347995,-16091435,94700640,17183454,85735982,90399615,-86251609,-68167910,-95327478,90586275,-99524469,16999817,27815883,-88279865,53092631,75125438,44270568,-23129316,-846252,-59608044,90938699,80923976,3534451,6218186,41256179,-9165388,-11897463,92423776,-38991231,-6082654,92275443,74040861,77457712,-80549965,-42515693,69918944,-95198414,15677446,-52451179,-50111167,-23732840,39520751,-90474508,-27860023,65164540,26582346,-20183515,99018741,-2826130,-28461563,-24759460,-83828963,-1739800,71207113,26434787,52931083,-33111208,38314304,-29429107,-5567826,-5149750,9582750,85289753,75490866,-93202942,-85974081,7365682,-42953023,21825824,68329208,-87994788,3460985,18744871,-49724457,-12982362,-47800372,39958829,-95981751,-71017359,-18397211,27941418,-34699076,74174334,96928957,44328607,49293516,-39034828,5945763,-47046163,10986423,63478877,30677010,-21202664,-86235407,3164123,8956697,-9003909,-18929014,-73824245]
    #res=s.fourSum_1(p,-236727523)
    #print res

    res=s.fourSum_1([0,0,0],0)
    print res