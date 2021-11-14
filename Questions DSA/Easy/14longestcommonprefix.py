# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
class Solution:
    #Time complexity:O(S) Where s is the length of the string
    #Space Complexity:O(1) Constant space is used
    
    def longestcommonprefix1(self,strs):
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        prefix = strs[0]
        prefix_length = len(prefix)
        for i in strs[1:]:
            while prefix!=i[:prefix_length]:
                prefix = prefix[:prefix_length-1]
                prefix_length-=1
            if len(prefix)==0:
                return ""
        return prefix
sol = Solution()
print(sol.longestcommonprefix1(["flower","flow","flight"]))
print(sol.longestcommonprefix1([]))
print(sol.longestcommonprefix1(["hello"]))