"""
217. Contains Duplicate

Description:
    Given an integer array nums, 
    return true if any value appears at least twice in the array,
    and return false if every element is distinct.

Example 1:
    Input: nums = [1,2,3,1]
    Output: true
    Explanation:
    The element 1 occurs at the indices 0 and 3.

Example 2:
    Input: nums = [1,2,3,4]
    Output: false
    Explanation:
    All elements are distinct.

Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

Constraints:
    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
"""            
# Set
# Complexity:
#     Time: O(n)
#     Space: O(n)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set = set()
        for num in nums:
            # 當 num 在 num_set 中 -> return True
            if num in num_set:
                return True
            # 當 num 不在 num_set 中 -> 加入 set
            num_set.add(num)
        
        # 沒有重複的數字 -> return False
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1,2,3,1]))
    print(s.containsDuplicate([1,2,3,4]))
    print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))