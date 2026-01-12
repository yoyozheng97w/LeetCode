"""
347. Top K Frequent Elements

Description:
    Given an integer array nums and an integer k, return the k most frequent elements. 
    You may return the answer in any order.
    
Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Example 3:
    Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
    Output: [1,2]

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.
"""
# Complexity:
#     Time: O(n㏒n)
#     Space: O(n)
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        numCnt = {} # num: cnt
        for num in nums:
            numCnt[num] = 1 + numCnt.get(num, 0)
        
        arr = []
        for num, cnt in numCnt.items():
            arr.append([cnt, num])
        arr.sort(reverse = True)

        res = []
        for i in range(k):
            res.append(arr[i][1])

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
    print(s.topKFrequent(nums = [1], k = 1))
    print(s.topKFrequent([1,2,1,2,1,2,3,1,3,2], k = 2))

