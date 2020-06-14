#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (44.67%)
# Likes:    13923
# Dislikes: 510
# Total Accepted:    2.7M
# Total Submissions: 5.9M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # a + b = target 
        # b = target - a
        bIndex = {}
        for i, a in enumerate(nums):
            if target - a in bIndex:
                return [bIndex[target-a], i]
            else:
                bIndex[a] = i
        return [-1, -1]
    
        
##import unittest
#
#class TestSolution(unittest.TestCase):
#    def setUp(self):
#        self.solution = Solution()
#    def test_0(self):
#        r = self.solution.twoSum([11,15], 9)
#        self.assertEqual(r,[-1,-1])
#    def test_1(self):
#        r = self.solution.twoSum([2,3], 5)
#        self.assertEqual(r,[0,1])
#    def test_one(self):
#        r = self.solution.twoSum([2,7,11,15], 9)
#        self.assertEqual(r,[0,1])
#
#
#if __name__ == '__main__':
#    unittest.main()
#
           
# @lc code=end
