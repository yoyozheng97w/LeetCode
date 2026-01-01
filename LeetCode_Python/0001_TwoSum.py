"""
1. Two Sum

Description:
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, 
    and you may not use the same element twice.

    You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    
Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
"""
# Brute Force 
#     Complexity: 
#         Time: O(n²)
#         Space: O(1)
class Solution1:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
# dictionary 用 hash table 
#     Complexity:
#         Time: O(n)
#         Space: O(n)
class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i in range(len(nums)):
            if (target - nums[i] in dic):
                return [dic[target - nums[i]], i]
            dic[nums[i]] = i
            
if __name__ == '__main__':
    s1 = Solution1()
    s2 = Solution2()
    print(s1.twoSum([2, 7, 11, 15], 9))
    print(s2.twoSum([2, 7, 11, 15], 9))
    print(s1.twoSum([3, 2, 4], 6))
    print(s2.twoSum([3, 2, 4], 6))
    print(s1.twoSum([3, 3], 6))
    print(s2.twoSum([3, 3], 6))