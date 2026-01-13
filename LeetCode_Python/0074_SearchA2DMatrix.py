"""
74. Search a 2D Matrix

Description:
    You are given an m x n integer matrix matrix with the following two properties:
    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.
    Given an integer target, return true if target is in matrix or false otherwise.

    You must write a solution in O(log(m * n)) time complexity.

Example 1:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true

Example 2:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    Output: false

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104
"""

# Complexity:
#     Time: O(㏒m+㏒n) = O(㏒(m∗n))
#     Space: O(1)
class Solution1:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        top, bottom = 0, m - 1
        # 找最接近且 <= target 的列
        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][0] == target:
                return True
            elif matrix[row][0] > target:
                bottom = row - 1
            else:    # matrix[row][0] < target
                top = row + 1
        if top == -1:
            return False
        else:
            target_row = top - 1
        
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[target_row][mid]:
                return True
            elif matrix[target_row][mid] > target:
                right = mid - 1
            else:    #  matrix[target_row][mid] < target
                left = mid + 1
        return False

# Complexity:
#     Time: O(㏒(m∗n))
#     Space: O(1)
class Solution2:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:    # matrix[row][col] > target
                left = mid + 1
        return False

if __name__ == '__main__':
    s1 = Solution1()
    print(s1.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
    print(s1.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
    print(s1.searchMatrix(matrix = [[1,3]], target = 3))
    s2 = Solution2()
    print(s2.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
    print(s2.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
    print(s2.searchMatrix(matrix = [[1,3]], target = 3))