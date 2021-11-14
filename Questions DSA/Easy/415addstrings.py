# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
class Solution:
    #Brute Force method
    def addstrings1(self,num1,num2):
        return str(int(num1)+int(num2))
    #Time complexity: O(max(num1,num2))
    #Space complexity:O(max(num1,num2))
    def addstrings2(self,num1,num2):
        res = []
        carry = 0
        p1 = len(num1)-1
        p2 = len(num2)-1
        while p1>=0 or p2>= 0:
            x1 = ord(num1[p1])-ord("0") if p1 >=0 else 0
            x2 = ord(num2[p2])-ord("0") if p2 >=0 else 0
            value = (x1+carry+x2)%10
            carry = (x1+carry+x2)//10
            res.append(value)
            p1-=1
            p2-=1
        if carry:
            res.append(carry)
        return "".join(str(x) for x in res[::-1])

sol = Solution()
print(sol.addstrings2("0","77"))
print(sol.addstrings2("456","123"))
