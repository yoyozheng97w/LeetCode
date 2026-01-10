"""
54. Spiral Matrix

Description:
   Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

Example 2:
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
"""
# Complexity:
#     Time: O(n*m)
#     Space: O(1)
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, n-1
        top, bottom = 0, m-1
        res = []
        while left <= right and top <= bottom:
            # append top row elements
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1
            # append right column elements
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            if not (left <= right and top <= bottom):
                break
            
            # append bottom row elements (reverse order)
            for c in range(right, left - 1, -1):
                res.append(matrix[bottom][c])
            bottom -= 1
            # append left column elements
            for r in range(bottom, top - 1, -1):
                res.append(matrix[r][left])
            left += 1
        return res
            
if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
    print(s.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    print(s.spiralOrder(matrix = [[1]]))