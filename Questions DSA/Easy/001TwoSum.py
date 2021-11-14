# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twosum(self,nums,target):
        d = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value not in d:
                d[nums[i]] = i
            else:
                return [d[value],i]
        return [-1,-1]
sol = Solution()
print(sol.twosum([2,7,11,15],9))
print(sol.twosum([3,2,4],6))
print(sol.twosum([3,2,4],15))