"""
118. Pascal's Triangle
Description:
    Given an integer numRows, return the first numRows of Pascal's triangle.

Example 1:
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
    Input: numRows = 1
    Output: [[1]]
"""

# Complexity: 
#     Time: O(n²)
#     Space: O(n)
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = list([list] * numRows)
        for i in range(numRows):
            tmplist = []
            for j in range(i + 1):
                if(j == 0 or j == i):
                    tmplist.append(1)
                else:
                    tmplist.append(result[i-1][j-1] + result[i-1][j])
                result[i] = tmplist
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))
    print(s.generate(1))