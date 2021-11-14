# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
class Solution:
    #Approach1:
    #Time Complexity:O(N) where N is the length of the list
    #Space Complexity:O(N) where N is the output list
    def runningSum(self,nums):
        lst = []
        sum1 = 0
        for i in nums:
            sum1+=i
            lst.append(sum1)
        return lst
    #Approach2:
    #Time Complexity:O(N) where N is the length of the list
    #Space Complexity:O(1)
    def runningsum1(self,nums):
        sum1 = 0
        for i in range(len(nums)):
            sum1+=nums[i]
            nums[i] = sum1
        return nums
sol = Solution()
print(sol.runningSum([1,2,3,4]))
print(sol.runningsum1([1,2,3,4]))