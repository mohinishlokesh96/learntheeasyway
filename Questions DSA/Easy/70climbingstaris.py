# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
class Solution:
    #Approach1:
    #Time Complexity:O(N)
    #Space Complexity:O(1)
    def climbingstairs(self,n):
        if n==1:
            return 1
        elif n==2:
            return 2
        current = 0
        first = 1
        second = 2
        for i in range(3,n+1):
            current = first+second
            first = second
            second = current
        return current
    #Approach2:
    #Time Complexity:O(N)
    #Space Complexity:O(N)
    def climbingstairs1(self,n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        dp=[0]*(n+1)
        dp[1]=1
        dp[2] = 2
        for i in range(3,len(dp)):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
sol = Solution()
print(sol.climbingstairs(5))