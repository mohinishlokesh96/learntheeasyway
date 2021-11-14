# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
class Solution:
    #Approach1:
    #Time Complexity: O(n)
    #Space Complexity:O(n)
    def happynumber(self,n):
        freq = {}
        def squarenumber(n):
            n=str(n)
            length = len(n)
            sum1= 0
            for i in range(length):
                sum1+=int(n[i])**2
            return sum1
        while n !=1:
            sum1 = squarenumber(n)
            if sum1 in freq:
                return False
            freq[n] = sum1
            n = sum1
        return True
sol = Solution()
print(sol.happynumber(2))