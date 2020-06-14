#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (34.30%)
# Likes:    4775
# Dislikes: 449
# Total Accepted:    709.1K
# Total Submissions: 2.1M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#

# @lc code=start
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[high] < nums[mid]:
                low = mid + 1
            else:
                high = mid

        rot = low
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            realmid = (mid + rot) % len(nums)
            if target == nums[realmid]:
                return realmid
            elif target < nums[realmid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
                
                
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_one(self):
        r = self.solution.search([4,5,6,7,0,1,2], 0)
        self.assertEqual(r,4)
        r = self.solution.search([4,5,6,7,0,1,2], 3)
        self.assertEqual(r,-1)
        r = self.solution.search([0,1,2], 2)
        self.assertEqual(r,2)

#  if __name__ == '__main__':
#      unittest.main()

           
        
# @lc code=end
