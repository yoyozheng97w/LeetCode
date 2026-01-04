"""
977. Squares of a Stored Array

Description:
    Given an integer array nums sorted in non-decreasing order, 
    return an array of the squares of each number sorted in non-decreasing order.

Example 1:
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].

Example 2:
    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order
"""
# Complexity:
#     Time: O(n)
#     Space: 
#       如果算輸出 res: O(n) 
#       不算輸出 res: O(1)
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        l, r = 0, n-1
        res = [int] * n
        for i in range(n):
            if abs(nums[l]) > abs(nums[r]):
                res[n-1-i] = nums[l] ** 2
                l += 1
            else:
                res[n-1-i] = nums[r] ** 2
                r -= 1
        return res        
if __name__ == '__main__':
    s = Solution()
    print(s.sortedSquares([-4,-1,0,3,10]))
    print(s.sortedSquares([-7,-3,2,3,11]))
    