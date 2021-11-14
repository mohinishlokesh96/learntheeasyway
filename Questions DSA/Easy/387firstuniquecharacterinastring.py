# Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.
class Solution:
    #Time complexity:O(N) Where N is the length of the string
    #Space Complexity:O(1)
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1
        freq = {}
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]]+=1
        for i in range(len(s)):
            if freq[s[i]]==1:
                return i
        return -1
sol = Solution()
print(sol.firstUniqChar("leetcode"))
print(sol.firstUniqChar("loveleetcode"))
print(sol.firstUniqChar("aabb"))