"""
56. Merge Intervals

Description:
    Given an array of intervals where intervals[i] = [starti, endi], 
    merge all overlapping intervals, and return an array of 
    the non-overlapping intervals that cover all the intervals in the input.

Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104
"""
# Complexity:
#     Time: O(n)
#     Space: O(n)
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x: x[0])
        start, end = intervals[0][0], intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
                
            else:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
                
        res.append([start, end])
        return res
    
if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(s.merge([[1,4],[4,5]]))