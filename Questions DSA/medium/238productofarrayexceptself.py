# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
class Solution:
    #Approach1
    #Time Complexity:O(n^2)
    #Space Complexity:O(n)
    def productexceptself1(self,nums):
        lst = [0]*len(nums)
        for i in range(len(nums)):
            val = 1
            for j in range(len(nums)):
                if j!=i:
                    val*=nums[j]
            lst[i] = val
        return lst
    #Approach2
    #Time Complexity:O(n)
    #Spaec Complexity:O(n)
    def productexceptself2(self,nums):
        right = [1]*(len(nums))#[1,1,2,6]
        left = [1]*(len(nums))#[24,12,4,1]
        for i in range(1,len(right)):
            right[i] = right[i-1]*nums[i-1]
        for i in reversed(range(len(nums)-1)):
            left[i] = left[i+1]*nums[i+1]
        for i in range(len(left)):
            left[i] = left[i]*right[i]
        return left
sol = Solution()
print(sol.productexceptself1([1,2,3,4]))
print(sol.productexceptself2([-1,1,0,-3,3]))