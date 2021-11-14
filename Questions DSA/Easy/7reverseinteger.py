# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
class Solution:
    #Approach1:
    #Time Complexity:O(N) Type conversion
    #Space Complexity:O(1)
    def reverseinteger(self,x):
        reverseValue=int(str(abs(x))[::-1])
        if x > 0:
            reverseValue=reverseValue
        else:
            reverseValue=-reverseValue
        if pow(-2, 31) < reverseValue < pow(2, 31) - 1:
            return reverseValue
        else:
            return 0


sol = Solution()
print(sol.reverseinteger(-121))
print(sol.reverseinteger(0))
print(sol.reverseinteger(2147483648))