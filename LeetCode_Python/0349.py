"""
349. Intersection of Two Arrays

Description:
    Given two integer arrays nums1 and nums2, return an array of their intersection.
    Each element in the result must be unique and you may return the result in any order.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]
    Explanation: [4,9] is also accepted.
    
Constraints:
    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000
"""

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set()
        for num in nums1:
            set1.add(num)
        res = set()
        for num in nums2:
            if num in set1:
                res.add(num)
        return list(res)
    
if __name__ == '__main__':
    s = Solution()
    print(s.intersection([1,2,2,1], [2,2]))
    print(s.intersection([4,9,5], [9,4,9,8,4]))