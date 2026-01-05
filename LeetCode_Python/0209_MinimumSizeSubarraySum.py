"""
209. Minimum Size Subarray Sum

Description:
    Given an array of positive integers nums and a positive integer target, 
    return the minimal length of a subarray whose sum is greater than or equal to target.
    If there is no such subarray, return 0 instead.

Example 1:
    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
    Input: target = 4, nums = [1,4,4]
    Output: 1

Example 3:
    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0

Constraints:
    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 104
"""            

# Complexity:
#     Time: O(n)
#     Space: O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        cur_sum = 0
        min_len = len(nums) + 1
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum >= target:
                cur_sum -= nums[l]
                if min_len > r - l + 1:
                    min_len = r - l + 1
                l += 1

        if min_len == len(nums) + 1:
            return 0
        else:
            return min_len

if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
    print(s.minSubArrayLen(4, [1,4,4]))
    print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
    print(s.minSubArrayLen(15, [5,1,3,5,10,7,4,9,2,8]))