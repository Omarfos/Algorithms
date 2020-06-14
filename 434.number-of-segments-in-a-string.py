#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#
# https://leetcode.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (37.33%)
# Likes:    181
# Dislikes: 677
# Total Accepted:    69.8K
# Total Submissions: 186.1K
# Testcase Example:  '"Hello, my name is John"'
#
# Count the number of segments in a string, where a segment is defined to be a
# contiguous sequence of non-space characters.
# 
# Please note that the string does not contain any non-printable characters.
# 
# Example:
# 
# Input: "Hello, my name is John"
# Output: 5
# 
# 
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        #  last = -1

        #  # "a"
        #  # " "
        #  # "Hello,  my name is Jon"
        #  for i in range(len(s)):
        #      if s[i] == ' ':
        #          if i - last - 1 > 0:
        #              count += 1
        #          last = i

        #  if last < len(s) - 1:
        #      count += 1
        
        #  return count
        s += ' ' # sentinel
        for i in range(1, len(s)):
            if s[i] == ' ' and s[i-1] != ' ':
                count += 1
        return count
        
# @lc code=end
