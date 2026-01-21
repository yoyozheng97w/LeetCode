"""
412. Fizz Buzz

Description:
    Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.
        
Example 1:
    Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
    Input: n = 5
    Output: ["1","2","Fizz","4","Buzz"]

Example 3:
    Input: n = 15
    Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
"""
# Complexity:
#     Time: O(n)
#     Space: O(n)
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        dic = {
            3: "Fizz",
            5: "Buzz"
        }
        res = []
        for i in range(1, n + 1):
            output = ""
            for key in dic:
                if i % key == 0:
                    output += dic[key]
            if output == "":
                output = f"{i}"
            res.append(output)
        return res
    
if __name__ == '__main__':
    s = Solution()
    print(s.fizzBuzz(3))
    print(s.fizzBuzz(5))
    print(s.fizzBuzz(15))