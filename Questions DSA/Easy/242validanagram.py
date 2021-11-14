# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
class Solution:
    #Approach1
    #Time Complexity:O(NlogN)
    #Space Complexity:O(1)
    def isAnagram1(self,s,t):
        s = list(s)
        t = list(t)
        s1 = s.sort()
        t1 = t.sort()
        return s1==t1
    def isAnagram2(self,s,t):
        if len(s)!=len(t):
            return False
        freq1 = {}
        freq2 = {}
        for i in s:
            if i not in freq1:
                freq1[i]=1
            else:
                freq1[i]+=1
        for i in t:
            if i not in freq2:
                freq2[i]=1
            else:
                freq2[i]+=1
        for i in freq1:
            if i not in freq2:
                return False
            if freq1[i]!=freq2[i]:
                return False
        return True
sol = Solution()
print(sol.isAnagram1("anagram","nagaram"))
print(sol.isAnagram2("rat","car"))