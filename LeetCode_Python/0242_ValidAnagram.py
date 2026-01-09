"""
242. Valid Anagram

Description:
    Given two strings s and t, return true if t is an anagram of s,
    and false otherwise.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false


Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.
"""            
# dictionary (Hash Table 實作)
# Complexity:
#     Time: O(n)
#     Space: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT


if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram(s = "anagram", t = "nagaram"))
    print(s.isAnagram(s = "rat", t = "car"))