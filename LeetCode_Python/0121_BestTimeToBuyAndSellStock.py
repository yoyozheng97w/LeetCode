"""
121. Best Time to Buy and Sell Stock

Description:
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. 
    If you cannot achieve any profit, return 0.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.
"""
# Complexity:
#     Time: O(n)
#     Space: O(1)
class Solution:
    def maxProfix(self, prices: list[int]) -> int:
        n = len(prices)
        buy = prices[0]
        profit = 0
        tmp_profit = 0
        for i in range(1, n):
            if(prices[i] < buy):
                buy = prices[i]
            else:
                tmp_profit = prices[i] - buy

            profit = max(profit, tmp_profit)     
               
        return profit


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfix([7,1,5,3,6,4]))
    print(s.maxProfix([7,6,4,3,1]))
