# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1.Open brackets must be closed by the same type of brackets.
# 2.Open brackets must be closed in the correct order.
class Solution:
    def isValid(self,s):
        closedbrackets=")]}"
        brackets={")": "(", "]": "[", "}": "{"}
        stack=[]
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            else:
                if char in closedbrackets:
                    if stack[-1] == brackets[char]:
                        stack.pop(-1)
                    else:
                        return False
                else:
                    stack.append(char)
        return len(stack) == 0
sol = Solution()
print(sol.isValid(""))
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("([)]"))
print(sol.isValid("{[]}"))