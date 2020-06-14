#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (51.50%)
# Likes:    1343
# Dislikes: 104
# Total Accepted:    368K
# Total Submissions: 714.1K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 5
# Output:
# [
# ⁠[1],
# ⁠[1,1],
# ⁠[1,2,1],
# ⁠[1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#

# @lc code=start
class Solution(object):
    #  def generate(self, numRows):
    #      """
    #      :type numRows: int
    #      :rtype: List[List[int]]
    #      """
    #      r = []
    #      for i in range(numRows):
    #          r.append([1])
    #          if i > 0:
    #              for j in range(1,len(r[i-1])):
    #                  r[i].append(r[i-1][j-1] + r[i-1][j]) 
    #              r[i].append(1)
    #      return r
    def generate(self, numRows):
        pascal = [[1] * i for i in range(1,numRows+1)]
        for i in range(numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal

        
#  import unittest

#  class TestSolution(unittest.TestCase):
#      def setUp(self):
#          self.solution = Solution()
#      def test_one(self):
#          r = self.solution.generate(5)
#          print(r)
#          #self.assertEqual(r,)


#  if __name__ == '__main__':
#      unittest.main()

           
# @lc code=end
