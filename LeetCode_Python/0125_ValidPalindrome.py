"""
125. Valid Palindrome

Description:
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
    and removing all non-alphanumeric characters, 
    it reads the same forward and backward. 
    Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.
    
Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.
    
Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
"""
# Two Pointers
# Complexity:
#     Time: O(n)
#     Space: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while(left < right):
            # while left < right and not s[left].isalnum():
            while left < right and not isAlnum(s[left]):
                left += 1
            # while left < right and not s[right].isalnum():
            while left < right and not isAlnum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True 

def isAlnum(c:str) -> bool:
    if (ord('a') <= ord(c.lower()) <= ord('z')) or (ord('0') <= ord(c) <= ord('9')):
        return True
    else:
        return False
    
if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))
    print(s.isPalindrome(" "))
    print(s.isPalindrome("0P"))