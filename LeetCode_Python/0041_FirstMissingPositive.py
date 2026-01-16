"""
41. First Missing Positive

Description:
    Given an unsorted integer array nums. 
    Return the smallest positive integer that is not present in nums.
    You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
    Input: nums = [1,2,0]
    Output: 3
    Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
    Input: nums = [3,4,-1,1]
    Output: 2
    Explanation: 1 is in the array but 2 is missing.

Example 3:
    Input: nums = [7,8,9,11,12]
    Output: 1
    Explanation: The smallest positive integer 1 is missing.
    
Constraints:
    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
"""

# Complexity:
#     Time: O(n)
#     Space: O(1)
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # swap elements in the array
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        n = len(nums)
        
        # 當 0 < nums[i] <= n 時，把 nums[i] 放到 index i-1 的位置
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                swap(nums, i, nums[i] - 1)
        
        # Find the first missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all positive integers from 1 to n are present, return n + 1
        return n + 1   
        
        
        
s = Solution()
print(s.firstMissingPositive([3,4,-1,1]))

"""
note:
1. 
    for i in range(n):
        while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            swap(nums, i, nums[i] - 1)
2. 
    for i, num in enumerate(nums):
        while 0 < num <= n and num != nums[num - 1]:
            swap(nums, i, num - 1)

以上兩種結果是不同的
1. 是每次都用最新的 nums[i]，所以行為不同。
2. 的 num 是「舊值的快照」，不會隨著 swap 更新，

"""