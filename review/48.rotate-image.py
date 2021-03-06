#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image/description/
#
# algorithms
# Medium (55.51%)
# Likes:    2882
# Dislikes: 223
# Total Accepted:    396.2K
# Total Submissions: 713.7K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# You are given an n x n 2D matrix representing an image.
# 
# Rotate the image by 90 degrees (clockwise).
# 
# Note:
# 
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
# 
# Example 1:
# 
# 
# Given input matrix = 
# [
# ⁠ [1,2,3],
# ⁠ [4,5,6],
# ⁠ [7,8,9]
# ],
# 
# rotate the input matrix in-place such that it becomes:
# [
# ⁠ [7,4,1],
# ⁠ [8,5,2],
# ⁠ [9,6,3]
# ]
# 
# 
# Example 2:
# 
# 
# Given input matrix =
# [
# ⁠ [ 5, 1, 9,11],
# ⁠ [ 2, 4, 8,10],
# ⁠ [13, 3, 6, 7],
# ⁠ [15,14,12,16]
# ], 
# 
# rotate the input matrix in-place such that it becomes:
# [
# ⁠ [15,13, 2, 5],
# ⁠ [14, 3, 4, 1],
# ⁠ [12, 6, 8, 9],
# ⁠ [16, 7,10,11]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #  def helper(m, n, inner):
        #      if inner >= n // 2:
        #          return
        #      for i in range(inner, n-1-inner):
        #          t = m[inner][i] # 1
        #          r = m[i][n-1-inner] # 2
        #          b = m[n-1-inner][n-1-i] # 4
        #          l = m[n-1-i][inner] # 3
                
        #          m[inner][i] = l
        #          m[i][n-1-inner] = t
        #          m[n-1-inner][n-1-i] = r
        #          m[n-1-i][inner] = b
        #      helper(m, n, inner + 1)

        #  helper(matrix, len(matrix), 0)
        #  return matrix

        n = len(matrix)
        for i in range(n//2):
            for j in range(n - n//2):
                a[i][j] = a[n - 1 - j][i]
        
# @lc code=end
