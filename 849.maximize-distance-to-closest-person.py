#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#
# https://leetcode.com/problems/maximize-distance-to-closest-person/description/
#
# algorithms
# Easy (42.48%)
# Likes:    745
# Dislikes: 101
# Total Accepted:    60.2K
# Total Submissions: 141.7K
# Testcase Example:  '[1,0,0,0,1,0,1]'
#
# In a row of seats, 1 represents a person sitting in that seat, and 0
# represents that the seat is empty. 
# 
# There is at least one empty seat, and at least one person sitting.
# 
# Alex wants to sit in the seat such that the distance between him and the
# closest person to him is maximized. 
# 
# Return that maximum distance to closest person.
# 
# 
# Example 1:
# 
# 
# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (seats[2]), then the closest person has
# distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# 
# 
# Example 2:
# 
# 
# Input: [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# 
# 
# 
# 
# 
# Constraints:
# 
# 
# 2 <= seats.length <= 20000
# seats contains only 0s or 1s, at least one 0, and at least one 1.
# 
# 
#

# @lc code=start
import math

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        last, n = -1, len(seats)
        res = 0

        # 1 0 0 0
        for i, seat in enumerate(seats):
            if seat:
                res = max(res, i if last < 0 else (i - last) // 2)
                last = i
        return max(res, n - last - 1)
                

        #  i = 0
        #  while i < len(seats) and seats[i] == 0:
        #      i += 1

        #  j = len(seats) - 1
        #  while j > i and seats[j] == 0:
        #      j -= 1

        #  max_zeros = max(i, len(seats) - j - 1)

        #  count = 0
        #  for k in range(i, j+1):
        #      if seats[k] == 0:
        #          count += 1
        #      else: 
        #          max_zeros = max(max_zeros, math.ceil(count / 2))
        #          count = 0

        #  return max_zeros
                
        
# @lc code=end
