# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).
class Solution:
    #Approach1:(Recursion)
    #Time complexity:O(2^N)
    #Space complexity:O(N) Stack size
    def fib1(self, N):
        if N <= 1:
            return N
        return self.fib1(N-1) + self.fib1(N-2)
    #Approach2:(Top-Down Approach)
    #Time complexity :O(N)
    #Space Complexity:O(N)
    def fib2(self, n):
        if n ==0:
            return 0
        elif n==1 or n==2:
            return 1
        d = [0]*(n+1)
        d[1] = 1
        d[2] = 1
        for i in range(2,n+1):
            d[i] = d[i-1]+d[i-2]
        return d[n]
    #Approach3:(Top-Down Approach Better Space Complexity)
    #Time complexity :O(N)
    #Space Complexity:O(1)
    def fib3(self, N):
        if (N <= 1):
            return N
        if (N == 2):
            return 1
        current = 0
        prev1 = 1
        prev2 = 1
        for i in range(3, N+1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return current

sol = Solution()
print(sol.fib1(4))
print(sol.fib2(3))
print(sol.fib3(2))