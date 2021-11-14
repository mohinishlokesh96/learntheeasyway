# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
class Solution:
    #Brute Force solution
    #Time Complexity:O(N^2) Where N is the length of nums
    #Space Complexity:O(1)
    def maxSubArray1(self,nums):
        max_subarray=float("-inf")
        for i in range(len(nums)):
            current_subarray=0
            for j in range(i, len(nums)):
                current_subarray+=nums[j]
                max_subarray=max(max_subarray, current_subarray)

        return max_subarray
    #Kadane Algorthim
    #Time Complexity:O(N) where N is the length of Nums
    #Space Complexity:O(1)
    def maxSubArray2(self,nums):
        max_value = float("-inf")
        sum1 = 0
        for i in nums:
            sum1+=i
            max_value = max(max_value,sum1)
            if sum1<0:
                sum1=0
        return max_value
sol = Solution()
print(sol.maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))
print(sol.maxSubArray2([1]))
print(sol.maxSubArray2([5,4,-1,7,8]))
