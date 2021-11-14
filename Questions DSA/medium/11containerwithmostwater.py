# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
class Solution:
    #Approach1:
    #Time Compelxity:O(n)
    #Space Complexity:O(1)
    def maxArea(self, height):
        left=0
        right=len(height) - 1
        area=0
        while left < right:
            area=max(area, (right - left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right-=1
            else:
                left+=1
        return area
sol = Solution()
print(sol.maxArea([1,1]))
print(sol.maxArea([4,3,2,1,4]))