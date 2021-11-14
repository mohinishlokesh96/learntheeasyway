# Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    #Approach1:
    #Time Complexity:O(n)
    #Space Complexity:O(1)
    def lengthOfLongestSubstring(self, s):
        if len(s)==0:
            return -1
        freq={}
        start=0
        max_length=0
        for end in range(len(s)):
            right_char=s[end]
            if right_char in freq:
                start=max(start, freq[right_char] + 1)
            freq[right_char]=end
            max_length=max(max_length, end - start + 1)
        return max_length
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))