#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (33.55%)
# Likes:    2205
# Dislikes: 556
# Total Accepted:    356.8K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#

# @lc code=start
class Solution:
    #  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #      if not matrix:
    #          return []

    #      tr, br = 0, len(matrix) - 1
    #      lc, rc = 0, len(matrix[0]) - 1 
    #      res = []


    #      while tr <= br and lc <= rc:
    #          # right
    #          for i in range(lc, rc + 1):
    #              res.append(matrix[tr][i])
    #          tr += 1

    #          # down
    #          for i in range(tr, br + 1):
    #              res.append(matrix[i][rc])
    #          rc -= 1

    #          # left
    #          if tr <= br:
    #              for i in reversed(range(lc, rc + 1)):
    #                  res.append(matrix[br][i])
    #          br -= 1

    #          # up
    #          if lc <= rc:
    #              for i in reversed(range(tr, br + 1)):
    #                  res.append(matrix[i][lc])
    #          lc += 1

    #      return res
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        n = len(matrix) 
        m = len(matrix[0]) 
        di, dj = 0, 1
        i, j = 0, 0
        for _ in range(m * n):
            res.append(matrix[i][j])
            matrix[i][j] = 'x' #seen
            if i + di < n and j + dj < m:
                if matrix[(i+di)%n][(j+dj)%m] == 'x':
                    di, dj = dj, -di
            i += di
            j += dj
        return res
        
# @lc code=end
