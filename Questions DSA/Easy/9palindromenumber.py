# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
class Solution:
    #Approach1
    #Time Complexity:O(N)
    #Space Complexity:O(1)
    def isPalindrome1(self, x):
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]
    def isPalindrome2(self,x):
        if x <0:
            return False
        palin = 0
        temp = x
        while x>0:
            div = x%10
            palin = palin*10+div
            x = x//10
        return temp==palin
sol = Solution()
print(sol.isPalindrome2(-122))
print(sol.isPalindrome2(121))