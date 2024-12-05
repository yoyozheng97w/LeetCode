"""
350. Intersection of Two Arrays II

Description:
    Given two integer arrays nums1 and nums2, return an array of their intersection. 
    Each element in the result must appear as many times as it shows in both arrays 
    and you may return the result in any order.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]

Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [4,9]
    Explanation: [9,4] is also accepted.
 
Constraints:
    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000
"""


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dic1 = {}
        for i in range(len(nums1)):
            if nums1[i] in dic1:
                dic1[nums1[i]] += 1
            else:
                dic1[nums1[i]] = 1
        res = []
        for num in nums2:
            if num in dic1 and dic1[num] > 0:
                res.append(num)
                dic1[num] -= 1
        return res
    
if __name__ == '__main__':
    s = Solution()
    print(s.intersect([1,2,2,1], [2,2]))
    print(s.intersect([4,9,5], [9,4,9,8,4]))