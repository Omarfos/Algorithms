#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (57.46%)
# Likes:    3649
# Dislikes: 120
# Total Accepted:    812.3K
# Total Submissions: 1.4M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
#
# @lc code=start
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        i = -1 
        for j, num in enumerate(nums):
            if nums[j] != 0:
                i = i + 1
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp 



#  import unittest

#  class TestSolution(unittest.TestCase):
#      def setUp(self):
#          self.solution = Solution()
#      def test_one(self):
#          nums = [0,1,0,3,12]
#          r = self.solution.moveZeroes(nums)
#          self.assertEqual(nums,[1,3,12,0,0])


#  if __name__ == '__main__':
#      unittest.main()

           
        
# @lc code=end
