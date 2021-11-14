# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2
class Solution:
    #Approach1:(Sorting)
    #Time Complexity:O(NlogN)
    #Space Complexity:O(len(nums1))
    def meargesortedarray(self,nums1,m,nums2,n):
        for i in range(m):
            nums1[i+m] = nums2[i]
        nums1.sort()
        return nums1
    #Approach2:(Two Pointers)
    #Time complexity:O(n+m)
    #Space complexity:O(1)
    def meargesortedarray1(self,nums1,m,nums2,n):
        nums1_copy=nums1[:m]
        p1=0
        p2=0
        for p in range(n + m):
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p]=nums1_copy[p1]
                p1+=1
            else:
                nums1[p]=nums2[p2]
                p2+=1
        return nums1
sol=Solution()
print(sol.meargesortedarray1([1,2,3,0,0,0],3,[2,5,6],3))