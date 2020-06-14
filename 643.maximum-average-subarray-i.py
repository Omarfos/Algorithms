#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
# https://leetcode.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (41.29%)
# Likes:    675
# Dislikes: 111
# Total Accepted:    75.2K
# Total Submissions: 182.2K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# Given an array consisting of n integers, find the contiguous subarray of
# given length k that has the maximum average value. And you need to output the
# maximum average value.
# 
# Example 1:
# 
# 
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].
# 
# 
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # initial window
# Input: [1,12,-5,-6,50,3], k = 4
        cur = 0
        for i in range(k):
            cur += nums[i]

        max_sum = cur
        for i in range(k, len(nums)):
            cur += nums[i] - nums[i - k]
            max_sum = max(max_sum, cur)

        return max_sum / k
                
#  import unittest 
#  class TestSolution(unittest.TestCase):
#      def setUp(self):
#          self.solution = Solution()
#      def test_one(self):
#          r = self.solution.findMaxAverage([1,12,-5,-6,50,3], 4)
#          self.assertEqual(r,12.75)


#  if __name__ == '__main__':
#      unittest.main()

           
        
# @lc code=end
