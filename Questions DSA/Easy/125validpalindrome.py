# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

class Solution:
    #Approach 1
    #Time Complexity:O(n)
    #Space Complexity:O(1)
    def isPalindrome1(self,s):
        lst = []
        for i in s:
            if i.isalnum():
                lst.append(i)
        s1 = "".join(lst).lower()
        return s1==s1[::-1]
    #Apprach2
    #Time complexity:O(n)
    #Space complexity:O(1)
    def isPalindrom2(self,s):
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
sol = Solution()
print(sol.isPalindrom2("race a car"))
print(sol.isPalindrome1("A man, a plan, a canal: Panama"))