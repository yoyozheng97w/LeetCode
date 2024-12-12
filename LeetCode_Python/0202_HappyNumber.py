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
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1

Example 2:
    Input: n = 2
    Output: false

Constraints:
    1 <= n <= 231 - 1
"""
# Complexity:
#     Time: O(㏒n)
#     Space: O(㏒n)
import time
class Solution1:
    def isHappy(self, n: int) -> bool:
        def getDigitSquare(n: int) -> int:
            sum = 0
            while(n):
                sum += pow(n % 10, 2)
                n = n // 10
            return sum

        sumSet = set()
        while (n != 1):
            n = getDigitSquare(n)
            if n in sumSet:
                break
            else:
                sumSet.add(n)
            
        if n == 1:
            return True
        else:
            return False
        
        
class Solution2:
    def getDigitSquare(self, n: int) -> int:
        sum = 0
        while(n):
            sum += pow(n % 10, 2)
            n = n // 10
        return sum

    def isHappy(self, n: int) -> bool:
        sumSet = set()
        while (n != 1):
            n = self.getDigitSquare(n)
            # n = sum(int(i) ** 2 for i in str(n))
            if n in sumSet:
                return False
            else:
                sumSet.add(n)

        return True

if __name__ == '__main__':
    s1 = Solution1()
    t1 = time.time()
    print(s1.isHappy(19))
    print(s1.isHappy(2))
    print(s1.isHappy(1111111))
    print(f"s1 run time: {time.time() - t1}")

    s2 = Solution2()
    t2 = time.time()
    print(s2.isHappy(19))
    print(s2.isHappy(2))
    print(s2.isHappy(1111111))
    print(f"s2 run time: {time.time() - t2}")