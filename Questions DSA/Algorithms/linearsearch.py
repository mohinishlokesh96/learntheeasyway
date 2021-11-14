#We will performing a linear scan or a linear search on a list or an Array
#Time Complexity:O(n) N is the number elements in a list or an array
class Solution:
    def linearsearch(self,nums,target):
        for i in nums:
            if target == i:
                return True
        return False
sol= Solution()
print(sol.linearsearch([1,2,3,4,5,6,7,8,9,10],5))
print(sol.linearsearch([1,2,3,4,5,6,7,8,9,10],11))