"""
202. Happy Number

Description:
    Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), 
    or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.
    Return true if n is a happy number, and false if not.

Example 1:
    Input: n = 19
    Output: true
    Explanation:
    1² + 9² = 82
    8² + 2² = 68
    6² + 8² = 100
    1² + 0² + 02 = 1

Example 2:
    Input: n = 2
    Output: false

Constraints:
    1 <= n <= 231 - 1
"""
# Complexity:
#     Time: O(㏒n)
#     Space: O(㏒n)
class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.getDigitSquare(n)
            if n == 1:
                return True
            
        return False
    
    def getDigitSquare(self, n: int) -> int:
        sum = 0
        while(n):
            sum += (n % 10) ** 2
            n = n // 10
        return sum

if __name__ == '__main__':
    s1 = Solution()
    print(s1.isHappy(19))
    print(s1.isHappy(2))
    print(s1.isHappy(1111111))