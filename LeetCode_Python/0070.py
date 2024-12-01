"""
70. Climbing Stairs

Description:
    You are climbing a staircase. 
    It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. 
    In how many distinct ways can you climb to the top?

Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

Constraints:
    1 <= n <= 45
"""

# Complexity:
#     Time: O(2ⁿ)
#     Space: O(n)
class Solution1:
    def climbStairs(self, n: int) -> int:
        if(n <= 2):
            return n
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)
# Complexity:
#     Time: O(n)
#     Space: O(n)
class Solution2:
    def climbStairs(self, n: int) -> int:
        res = [0] * (n+1)
        for i in range(n+1):
            if (i <= 2):
                res[i] = i
            else:
                res[i] = res[i - 1] + res[i - 2]

        return res[n]

# Complexity:
#     Time: O(n)
#     Space: O(1)
class Solution3:
    def climbStairs(self, n: int) -> int:
        prev1 = 1
        prev2 = 1
        for i in range(n - 1):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur
        return cur

if __name__ == '__main__':
    s1 = Solution1()
    print(s1.climbStairs(2))
    print(s1.climbStairs(4))
    s2 = Solution2()
    print(s2.climbStairs(2))
    print(s2.climbStairs(4))
    s3 = Solution3()
    print(s3.climbStairs(2))
    print(s3.climbStairs(4))