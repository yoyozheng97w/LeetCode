"""
1768. Merge Strings Alternately

Description:
    You are given two strings word1 and word2. 
    Merge the strings by adding letters in alternating order, starting with word1. 
    If a string is longer than the other, 
    append the additional letters onto the end of the merged string.
    Return the merged string.

Example 1:
    Input: word1 = "abc", word2 = "pqr"
    Output: "apbqcr"
    Explanation: The merged string will be merged as so:
    word1:  a   b   c
    word2:    p   q   r
    merged: a p b q c r

Example 2:
    Input: word1 = "ab", word2 = "pqrs"
    Output: "apbqrs"
    Explanation: Notice that as word2 is longer, "rs" is appended to the end.
    word1:  a   b 
    word2:    p   q   r   s
    merged: a p b q   r   s

Example 3:
    Input: word1 = "abcd", word2 = "pq"
    Output: "apbqcd"
    Explanation: Notice that as word1 is longer, "cd" is appended to the end.
    word1:  a   b   c   d
    word2:    p   q 
    merged: a p b q c   d
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        i = 0
        result = ''
        while(n1 > i or n2 > i):
            if(n1 > i): result += word1[i]
            if(n2 > i): result += word2[i]
            i += 1
        return result


if __name__ == '__main__':
    s = Solution()
    
    word1 = "abc"
    word2 = "pqr"

    word11 = "ab"
    word22 = "pqrs"

    word111 = "abcd"
    word222 = "pq"

    print(s.mergeAlternately(word1, word2))
    print(s.mergeAlternately(word11, word22))
    print(s.mergeAlternately(word111, word222))
    
