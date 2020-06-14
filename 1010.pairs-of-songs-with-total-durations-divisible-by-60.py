#
# @lc app=leetcode id=1010 lang=python
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
#
# algorithms
# Easy (47.47%)
# Likes:    457
# Dislikes: 37
# Total Accepted:    31.5K
# Total Submissions: 66.4K
# Testcase Example:  '[30,20,150,100,40]'
#
# In a list of songs, the i-th song has a duration of time[i] seconds. 
# 
# Return the number of pairs of songs for which their total duration in seconds
# is divisible by 60.  Formally, we want the number of indices i, j such that i
# < j with (time[i] + time[j]) % 60 == 0.
# 
# 
# 
# Example 1:
# 
# 
# Input: [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
# 
# 
# 
# Example 2:
# 
# 
# Input: [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible
# by 60.
# 
# 
# Note:
# 
# 
# 1 <= time.length <= 60000
# 1 <= time[i] <= 500
# 
# 
#

# @lc code=start
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        # Input: [30,20,150,100,40]
        # bruteforce
        #  pairs = 0
        #  for i, t1 in enumerate(time):
        #      for j, t2 in enumerate(time[i+1:]):
        #          if (t1 + t2) % 60 == 0:
        #              pairs += 1

        # Hashtable: 

        # Input: [30,20,150,100,40]
        # {30: 2, 20: 1, 
        # [40, 140]
        # [30, 150]
        # [20, 160]
        # [60, 60] 
        # [120, 120]
        # [59, 1]

        pairs = 0
        hashtable = {}
        for t in time:
            if t % 60 == 0:
                pairs += hashtable.get(0,0)
            else:
                pairs += hashtable.get(60 - (t % 60), 0)
            hashtable[t % 60] = hashtable.get(t % 60, 0) + 1

        return pairs
        
# @lc code=end
