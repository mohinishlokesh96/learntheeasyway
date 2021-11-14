# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
class Solution:
    def movezeros(self,nums):
        #Approach1:
        #Time Complexity:O(N)
        #Space Complexity:O(N)
        left = 0
        count = len(nums)
        while count>left:
            if nums[left]==0:
                nums.append(0)
                del nums[left]
                count-=1
            else:
                left+=1
        return nums
sol = Solution()
print(sol.movezeros([4,2,4,0,0,3,0,5,1,0]))