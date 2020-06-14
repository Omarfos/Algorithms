#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (50.10%)
# Likes:    4846
# Dislikes: 216
# Total Accepted:    841.7K
# Total Submissions: 1.7M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# If you were only permitted to complete at most one transaction (i.e., buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
# 
# Note that you cannot sell a stock before you buy one.
# 
# Example 1:
# 
# 
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
# 
# 
# Example 2:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
# 
#

# @lc code=start
from typing import List
import sys

class Solution:
    #  def maxProfit(self, prices: List[int]) -> int:
    #      # brutefore
    #      max_profit = 0
    #      for i, buy_price in enumerate(prices):
    #          for sell_price in prices[i+1:]:
    #              max_profit = max(max_profit, sell_price - buy_price)
    #      return max_profit

    #  def maxProfit(self, prices: List[int]) -> int:
    #      # idea, when we encouter a new min, the prev min is obsolete
    #      # dynamic programming can be used to memoize the prev min encountered
    #      if len(prices) <= 1:
    #          return 0

    #      max_profit = 0
    #      local_min = prices[0]
    #      for i, price in enumerate(prices[1:]):
    #          local_min = min(local_min, price)
    #          max_profit = max(max_profit, price - local_min)
    #      return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        # idea, instead of looking at the prices of each day, let's look at the
        # changes, this problem then transforms to finding the maximum subarray
        # divide and conquer solution

        if len(prices) <= 1:
            return 0
        # Transform into changes
        diffs = [0]
        for i in range(1, len(prices)):
            diffs.append(prices[i] - prices[i-1])
        return self.maxProfitDivideConquer(diffs, 0, len(diffs) - 1)
    
    def maxProfitDivideConquer(self, prices, low, high):
        if low == high:
            return prices[low]
        else:
            mid = (low + high) // 2
            leftSum = self.maxProfitDivideConquer(prices, low, mid)
            rightSum = self.maxProfitDivideConquer(prices, mid+1, high)
            crossingSum = self.maxCrossingSum(prices, low, mid, high)
            return max(leftSum, rightSum, crossingSum)

    def maxCrossingSum(self, prices, low, mid, high):
        leftSum = rightSum = float('-inf')
        
        curSum = 0
        for i, price in enumerate(reversed(prices[low:mid+1])):
            curSum += price
            leftSum = max(leftSum, curSum)

        curSum = 0
        for i, price in enumerate(prices[mid+1:high+1]):
            curSum += price
            rightSum = max(rightSum, curSum)
        return leftSum + rightSum


        
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_one(self):
        r = self.solution.maxProfit([7,1,5,3,6,4])
        self.assertEqual(r,5)
        r = self.solution.maxProfit([7,6,4,3,1])
        self.assertEqual(r,0)


#  if __name__ == '__main__':
#      unittest.main()

           
# @lc code=end
