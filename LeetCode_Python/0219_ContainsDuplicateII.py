"""
219. Contains Duplicate II

Description:
    Given an integer array nums and an integer k, 
    return true if there are two distinct indices i and j in the array 
    such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true

Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true

Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false

Constraints:
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    0 <= k <= 105
"""            
# dictionary (Hash Table 實作)
# Complexity:
#     Time: O(n)
#     Space: O(n)
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dic = {} # key(num): value(index)
        for index, num in enumerate(nums):
            if num in dic and index - dic[num] <= k:
                return True
            dic[num] = index
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyDuplicate([1,2,3,1], 3))
    print(s.containsNearbyDuplicate([1,0,1,1], 1))
    print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))