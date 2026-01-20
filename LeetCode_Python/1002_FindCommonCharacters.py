"""
1002. Find Common Characters

Description:
    Given a string array words, 
    return an array of all characters that show up in all strings within the words 
    (including duplicates).
    You may return the answer in any order.

Example 1:
    Input: words = ["bella","label","roller"]
    Output: ["e","l","l"]

Example 2:
    Input: words = ["cool","lock","cook"]
    Output: ["c","o"]

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of lowercase English letters.
"""

# Complexity:
#     Time: O(n*k)
#     Space: O(n)
from collections import Counter
class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        cnt = Counter(words[0])
        for word in words:
            cur_cnt = Counter(word)
            for c in cnt:
                cnt[c] = min(cnt[c], cur_cnt[c])
        res = []
        for key in cnt:
            for i in range(cnt[key]):
                res.append(key)
        return res    

if __name__ == '__main__':
    s = Solution()
    print(s.commonChars(["bella","label","roller"]))
    print(s.commonChars(["cool","lock","cook"]))
    