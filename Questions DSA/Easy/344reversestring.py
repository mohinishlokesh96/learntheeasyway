# Write a function that reverses a string. The input string is given as an array of characters s.
class Solution:
    #Approach1:(Recursion)
    #Time Complexity:O(N)
    #Space Complexity:O(N)
    def reverseString1(self,s):
        def helper(left, right):
            if left < right:
                s[left], s[right]=s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)
        return s

    #Approach2:(Two Pointer)
    #Time complexity:O(N)
    #Space Complexity:O(1)
    def reverseString2(self,s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        return s

sol = Solution()
print(sol.reverseString1(["h","e","l","l","o"]))
print(sol.reverseString2(["h","e","l","l","o"]))