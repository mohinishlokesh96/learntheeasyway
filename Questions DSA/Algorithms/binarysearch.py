#This is the second searching algorithm which is used in searching an element in a sorted array,
#The algo works by splitting the sorted array into half and thereby reducing the time complexity by half
#Time complexity:O(logN)
class Solution:
    def binarysearch(self,nums,target):
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            if target>nums[mid]:
                left = mid+1
            else:
                right = mid-1
        return -1
sol = Solution()
print(sol.binarysearch([1,2,3,4,5,6,7,8,9,10],6))
print(sol.binarysearch([1,2,3,4,5,6,7,8,9,10],11))