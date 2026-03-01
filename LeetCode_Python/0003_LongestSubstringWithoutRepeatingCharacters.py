"""
3. Longest Substring Without Repeating Characters

Description:
    Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 2:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 1:
    Input: s = "dvdf"
    Output: 3

Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""
# My Sloution
# Complexity:
#     Time: O(n)
#     Space: O(n)
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        dic = {}
        start = 0
        for i, c in enumerate(s):
            if c in dic:
                start = max(start, dic[c] + 1)
            else:
                pass

            dic[c] = i
            
            max_length = max(max_length, i - start + 1)
        return max_length

# NeatCode
# Complexity:
#     Time: O(n)
#     Space: O(n)
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, length = 0, 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
                
            charSet.add(s[r])
            length = max(length, r - l + 1)

        return length
            
if __name__ == '__main__':
    s1 = Solution1()
    print(s1.lengthOfLongestSubstring("abcabcbb"))   # 3
    print(s1.lengthOfLongestSubstring("bbbbb"))      # 1
    print(s1.lengthOfLongestSubstring("pwwkew"))     # 3
    print(s1.lengthOfLongestSubstring("dvdf"))       # 3
    print(s1.lengthOfLongestSubstring("abba"))       # 2

    s2 = Solution2()
    print(s2.lengthOfLongestSubstring("abcabcbb"))   # 3
    print(s2.lengthOfLongestSubstring("bbbbb"))      # 1
    print(s2.lengthOfLongestSubstring("pwwkew"))     # 3
    print(s2.lengthOfLongestSubstring("dvdf"))       # 3
    print(s2.lengthOfLongestSubstring("abba"))       # 2