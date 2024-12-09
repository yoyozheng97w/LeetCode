"""
3152. Special Array II
Description:
    An array is considered special if 
    every pair of its adjacent elements contains two numbers with different parity.

    You are given an array of integer nums and a 2D integer matrix queries, 
    where for queries[i] = [fromi, toi] your task is to check that subarray
        nums[fromi..toi] is special or not.

    Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

Example 1:
    Input: nums = [3,4,1,2,6], queries = [[0,4]]
    Output: [false]
    Explanation:
    The subarray is [3,4,1,2,6]. 2 and 6 are both even.

Example 2:
    Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]
    Output: [false,true]
    Explanation:
    The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
    The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.

Constraints:
    1 <= nums.length <= 105
    1 <= nums[i] <= 105
    1 <= queries.length <= 105
    queries[i].length == 2
    0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
"""

# Complexity:
#     Time: O(n * k)
#     Space: O(1)
# Time Limit Exceeded
class Solution1:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        res = []
        for q in queries:
            start = q[0]
            end = q[1]
            isSpecial = True
            for i in range(start, end):
                if nums[i] % 2 == nums[i + 1] % 2:
                    isSpecial = False
                    break
            res.append(isSpecial)
        return res
    
# Complexity:
#     Time: O(n)
#     Space: O(n)
class Solution2:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        n = len(nums)
        res = []
        specialArr = [0] * n
        # specialArr[i]: nums[i] 到前幾個數列為 special
        # 例：specialArr[4] = 2 -> nums[4] ~ nums[2] 是 special array
        for i in range(n - 1):
            if nums[i + 1] % 2 != nums[i] % 2:
                specialArr[i + 1] = specialArr[i] + 1
        for q in queries:
            if specialArr[q[1]] >= q[1] - q[0]:
                res.append(True)
            else:
                res.append(False)
        return res


if __name__ == '__main__':
    s2 = Solution2()
    print(s2.isArraySpecial([3,4,1,2,6], [[0,4]]))
    print(s2.isArraySpecial([4,3,1,6], [[0,2],[2,3]]))