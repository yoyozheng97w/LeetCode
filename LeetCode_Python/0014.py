"""
14. Longest Common Prefix

Description:
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.
"""
# Complexity:
#     Time: O(n * k)
#     Space: O(k)
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        n = len(strs)
        prefix_len = len(strs[0])
        res = strs[0]
        for i in range(1, n):
            while(res != strs[i][:prefix_len]):
                prefix_len -= 1
                res = res[:prefix_len]
                if prefix_len == 0:
                    return ""
        return res
        
if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
    print(s.longestCommonPrefix(["dog","racecar","car"]))
    