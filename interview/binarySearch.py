# 例：a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
"""
target = 6
l = 0, r = 9, mid = 4 -> target < arr[4] = 9
l = 0, r = 3, mid = 1 -> target > arr[1] = 3
l = 2, r = 3, mid = 2 -> target > arr[2] = 5
l = 3, r = 3, mid = 3 -> target < arr[3] = 7
l = 3, r = 2

target = 8
l = 0, r = 9, mid = 4 -> target < arr[4] = 9
l = 0, r = 3, mid = 1 -> target > arr[1] = 3
l = 2, r = 3, mid = 2 -> target > arr[2] = 5
l = 3, r = 3, mid = 3 -> target > arr[3] = 7
l = 4, r = 3

"""

# Complexity:
#     Time: O(n)
#     Space: O(1)
class Solution:
    def Bsearch(self, arr: list[int], target: int):
        n = len(arr)
        left, right = 0, n - 1
        while(left <= right):
            mid = (left + right) // 2
            if(arr[mid] == target):
                return target
            elif(arr[mid] > target):
                right = mid - 1
            else:    # (arr[mid] < target)
                left = mid + 1

        if(right == -1):
            return None
        elif(left == n):
            return arr[left - 1]
        else:
            # return arr[left - 1]
            return arr[right]
            
# s = Solution()
# print(s.Bsearch([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 11))
# print(s.Bsearch([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 14))
# print(s.Bsearch([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 6))
# print(s.Bsearch([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 8))
# print(s.Bsearch([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 0))
# print(s.Bsearch([], 1))
# print(s.Bsearch([1, 3, 4], 5))
# print(s.Bsearch([1, 3, 5], 4))
# print(s.Bsearch([1, 3, 5], 2))
# print(s.Bsearch([1, 3], 3))
# print(s.Bsearch([1, 3], 1))
# print(s.Bsearch([1, 3], 2))


class Solution2:
    def Bsearch(self, nums: list[int], target: int):
        n = len(nums)
        left, right = 0, n - 1
        if right == -1:
            return -1
        if (target < nums[0]):
            return -1
        elif (target > nums[n-1]):
            return nums[n-1]

        while left <= right:
            mid = left + ((right - left) // 2) 
            if nums[mid] == target:
                return nums[mid]
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return nums[right]
        # 返回最接近且小於 target 的值
        # print(f"right = {right}, mid = {ans}, nums[mid] = {nums[ans]}")
        # if nums[left] > target:
        #     left -= 1
        # return nums[left]
        # return nums[right] if right >= 0 else None
    
s = Solution2()
print(s.Bsearch([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 10))
print(s.Bsearch([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 14))
print(s.Bsearch([1, 3, 4, 9, 11, 13, 15, 17, 19, 21], 14))
print(s.Bsearch([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 6))
print(s.Bsearch([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 8))
# print(s.Bsearch([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 0))
print(s.Bsearch([3, 4, 6, 9], 5))
# print(s.Bsearch([3, 5, 6, 9], 10))
# print(s.Bsearch([], 1))
# print(s.Bsearch([1, 3, 4], 5))
print(s.Bsearch([1, 3, 5], 4))
print(s.Bsearch([1, 3, 5], 2))
print(s.Bsearch([1, 3], 3))
print(s.Bsearch([1, 3], 1))
print(s.Bsearch([1, 3], 2))