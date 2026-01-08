"""
20. Valid Parentheses

Description:
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "([])"
    Output: true

Example 2:
    Input: s = "([)]"
    Output: false

Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""
# Complexity:
#     Time: O(n)
#     Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for char in s:
            if char in dic.values():
                stack.append(char)
            elif not stack or dic[char] != stack.pop():
                return False
        if len(stack) != 0:
            return False
        else:
            return True

if __name__ == '__main__':
    s = Solution()
    print(s.isValid("([])"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("]"))