"""
1346. Check If N and Its Double Exist

Description:
    Given an array arr of integers, 
    check if there exist two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

Example 1:
    Input: arr = [10,2,5,3]
    Output: true
    Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:
    Input: arr = [3,1,7,11]
    Output: false
    Explanation: There is no i and j that satisfy the conditions.
"""

# Complexity:
#     Time: O(n)
#     Space: O(n)
class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        dic = {}
        for i in range(len(arr)):
            dic[arr[i]] = i

        for i in range(len(arr)):
            if (arr[i] * 2 in dic) and (dic[arr[i] * 2] != i):
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.checkIfExist([10,2,5,3]))
    print(s.checkIfExist([3,1,7,11]))
    