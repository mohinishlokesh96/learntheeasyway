# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
class Solution:
    #Approach1:
    #Time Complexity:O(N) Where N is the length of the list
    #Space Complexity:O(1)
    def maxProfit(self, prices):
        max_value=0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_value+=prices[i] - prices[i - 1]
        return max_value
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([1,2,3,4,5]))
print(sol.maxProfit([7,6,4,3,1]))
