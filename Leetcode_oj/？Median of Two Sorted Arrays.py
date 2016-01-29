class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        len_nums1=len(nums1)
        len_nums2=len(nums2)
        if len_nums1>len_nums2:
            return self.findMedianSortedArrays(nums2,nums1)
        if len_nums1==0:
            return nums2[len_nums2/2]
        if len_nums2==0:
            return nums1[len_nums1/2]
        mid_nums1=nums1[len_nums1/2]
        mid_nums2=nums2[len_nums2/2]
        while len(nums1)>1 and len(nums2)>1 :
            if mid_nums1==mid_nums2:
                return mid_nums1
            if mid_nums1<mid_nums2:
                len_nums1=len(nums1)
                nums1=nums1[len(nums1)/2:]
                nums2=nums2[0:len(nums2)-(len_nums1)/2]
            else:
                len_nums1=len(nums1)
                nums1=nums1[0:len(nums1)/2]
                nums2=nums2[len_nums1/2:]

            mid_nums1=nums1[(len(nums1))/2]
            mid_nums2=nums2[(len(nums2))/2]
        if len(nums1)==len(nums2)==1:
            if nums1[0]>nums2[0]:
                return nums2[0]
            else:
                return nums1[0]
        if len(nums1)==1:
            if nums1[0]>nums2[(len(nums2))/2]:
                nums2=nums2[1:]
                return nums2[(len(nums2))/2]
            else:
                nums2=nums2[:len(nums2)-1]
                return nums2[(len(nums2))/2]
        if len(nums2)==1:
            if nums2[0]>nums1[(len(nums1))/2]:
                nums1=nums1[1:]
                return nums1[(len(nums1))/2]
            else:
                nums1=nums1[:len(nums1)-1]
                return nums1[(len(nums1))/2]
        return nums1,nums2

    def findMedianSortedArrays_2(self, nums1, nums2):
        l1=len(nums1)
        l2=len(nums2)

        if l1==0:
            return nums2[l2/2]
        if l2==0:
            return nums1[l1/2]      

        if l1==l2==1:
            if nums1[0]>nums2[0]:
                return nums1[0]
            else:
                return nums2[0]
        if l1==1:
            if nums1[0]>nums2[l2/2]:
                nums2=nums2[1:]
                return nums2[(len(nums2))/2]
            else:
                nums2=nums2[:l2-1]
                return nums2[(len(nums2))/2]
        if l2==1:
            if nums2[0]>nums1[(l1)/2]:
                nums1=nums1[1:]
                return nums1[(len(nums1))/2]
            else:
                nums1=nums1[:l1-1]
                return nums1[(len(nums1))/2]
        
        if l1>l2:
            return self.findMedianSortedArrays_2(nums2,nums1)

        m1=nums1[l1/2]
        m2=nums2[l2/2]
        if m1==m2:
            return m1
        if m1<m2:
            nums1=nums1[l1/2:]
            nums2=nums2[0:l2-(l1)/2]
        else:
            nums1=nums1[0:(l1+1)/2]
            nums2=nums2[l1/2:]
        print nums1,nums2
        return self.findMedianSortedArrays_2(nums1,nums2)


if __name__ == '__main__':
    s=Solution()
    #print s.findMedianSortedArrays_2([1, 12, 15, 26, 38],[2, 13, 17, 30, 45])
    print s.findMedianSortedArrays_2([],[2, 13, 17, 30, 45])
