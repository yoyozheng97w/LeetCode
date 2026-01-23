"""
7. Reverse Integer

Description:
    Given a signed 32-bit integer x, return x with its digits reversed. 
    If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
    Input: x = 123
    Output: 321

Example 2:
    Input: x = -123
    Output: -321

Example 3:
    Input: x = 120
    Output: 21

Constraints:
    -231 <= x <= 231 - 1
""" 
#     Complexity: 
#         Time: O(㏒n)
#         Space: O(1)
class Solution:
    def reverse(self, x: int) -> int:
        positive = True if x > 0 else False
        res = 0
        x = abs(x)
        while(x):
            res = res * 10 + x % 10
            x = x // 10

        if res < -(2 ** 31) or res > 2 ** 31 - 1:
            return 0
        elif positive:
            return res
        else:
            return -res
            
if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(120))
    print(s.reverse(1534236469))