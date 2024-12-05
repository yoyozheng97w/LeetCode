"""
35. Search Insert Position

Description:
    Given a sorted array of distinct integers and a target value, 
    return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4
"""

# Complexity:
#     Time: O(logn)
#     Space: O(1)
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while(l <= r):
            m = (l + r) // 2
            if(nums[m] == target):
                return m
            elif(nums[m] > target):
                r = m - 1
            else:
                l = m + 1
        return l
    
if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 5))
    print(s.searchInsert([1, 3, 5, 6], 0))
    print(s.searchInsert([1, 3, 5, 6], 7))
    

"""
nums = [1, 3, 5, 6], target = 2
l = 0, r = 3, m = 1 -> nums[1] > target
l = 0, r = 0, m = 0 -> nums[0] < target
l = 1, r = 0
"""