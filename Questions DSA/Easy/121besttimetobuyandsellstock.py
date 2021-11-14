# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
class Solution:
    def maxProfit(self,prices):
        if len(prices)==0:
            return 0
        maxvalue = float("-inf")
        minvalue = float("inf")
        for i in prices:
            minvalue = min(minvalue,i)
            maxvalue = max(maxvalue,i-minvalue)
        return maxvalue
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([]))
print(sol.maxProfit([7,6,4,3,1]))