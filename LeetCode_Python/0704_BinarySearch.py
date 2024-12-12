"""
704. Binary Search

Desctiption:
    Given an array of integers nums which is sorted in ascending order, 
    and an integer target, write a function to search target in nums. 
    If target exists, then return its index. Otherwise, return -1.
    You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1
"""
# Complexity:
#     Time: O(㏒n)
#     Space: O(1)
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while(left <= right):
            mid = (left + right) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        return -1
    
if __name__ == '__main__':
    s = Solution()
    print(s.search([-1,0,3,5,9,12], 9))
    print(s.search([-1,0,3,5,9,12], 2))
    print(s.search([], 2))
    
        
