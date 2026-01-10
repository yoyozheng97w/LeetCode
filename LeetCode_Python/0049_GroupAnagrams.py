"""
49. Group Anagrams

Description:
    Given an array of strings strs, group the anagrams together. 
    You can return the answer in any order.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Explanation:
        There is no string in strs that can be rearranged to form "bat".
        The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
        The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3:
    Input: strs = ["a"]
    Output: [["a"]]
"""

# Complexity:
#     Time: O(n*k)
#     Space: O(n*k)
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            countChar = [0] * 26
            for c in s:
                countChar[ord(c) - ord('a')] += 1
            # Python 的字典 (dict) 的鍵 (key) 不能 是列表 (list)。
            # 字典的鍵必須是「可哈希的」(hashable) 且「不可變的」(immutable)。
            # list 是可變對象，若作為鍵會導致哈希值改變，無法穩定地查找。
            # 若需要以序列為鍵，請使用元組 (tuple) 代替。 
            res[tuple(countChar)].append(s)
        return list(res.values())
    
if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
    print(s.groupAnagrams([""]))
    print(s.groupAnagrams(["a"]))
