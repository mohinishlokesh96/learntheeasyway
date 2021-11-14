# Given an integer n, return a string array answer (1-indexed) where:
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i if non of the above conditions are true.
class Solution:
    #Time complexity:O(N)
    #space Complxity:O(N)
    def fizzbuzz(self,n):
        ans = []
        for num in range(1,n+1):
            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)
            if divisible_by_3 and divisible_by_5:
                ans.append("FizzBuzz")
            elif divisible_by_3:
                ans.append("Fizz")
            elif divisible_by_5:
                ans.append("Buzz")
            else:
                ans.append(str(num))
        return ans
sol = Solution()
print(sol.fizzbuzz(1))
print(sol.fizzbuzz(13))
print(sol.fizzbuzz(5))