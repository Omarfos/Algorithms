#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (33.54%)
# Likes:    1257
# Dislikes: 1853
# Total Accepted:    537.7K
# Total Submissions: 1.6M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        left, right = 0, x 
        while left < right:
            mid = (left + right) // 2
            if mid ** 2 <= x:
                left = mid 
            else:
                right = mid - 1

        # End Condition: left > right
        return left  


import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_one(self):
        r = self.solution.mySqrt(8)
        self.assertEqual(r,2)
        r = self.solution.mySqrt(4)
        self.assertEqual(r,2)
        r = self.solution.mySqrt(9)
        self.assertEqual(r,3)


if __name__ == '__main__':
    unittest.main()

           
        
# @lc code=end
