#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (46.16%)
# Likes:    7600
# Dislikes: 353
# Total Accepted:    995.4K
# Total Submissions: 2.2M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxProfitDivideConquer(nums, 0, len(nums) - 1)
    
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
# @lc code=end
