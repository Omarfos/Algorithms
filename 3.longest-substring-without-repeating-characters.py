#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (30.09%)
# Likes:    9069
# Dislikes: 549
# Total Accepted:    1.5M
# Total Submissions: 5.1M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 

# @lc code=start
 #  If we encounter a duplicate, the next substring must start at the index of the previous
 #  encouter + 1
 #  Incremetal Algorithm:
 #      is it a new char?
 #          cur substring len += 1
 #          indices[char] = index
 #      otherwise:
 #          max = max(cur - start + 1, max)
 #          start = max(start, prev_encounter_index + 1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        r = start = 0
        indices = {}
        # pwwkew
        for i, c in enumerate(s):
            if c in indices:
                start = max(start, indices[c] + 1)
            r = max(r, i - start + 1)
            indices[c] = i
        return r
                
#  import unittest

#  class TestSolution(unittest.TestCase):
    #  def setUp(self):
        #  self.solution = Solution()
    #  def test_one(self):
        #  r = self.solution.lengthOfLongestSubstring("pwwkew")
        #  self.assertEqual(r,3)
    #  def test_two(self):
        #  r = self.solution.lengthOfLongestSubstring("aaaa")
        #  self.assertEqual(r,1)
    #  def test_three(self):
        #  r = self.solution.lengthOfLongestSubstring("abcabcbb")
        #  self.assertEqual(r,3)

#  if __name__ == '__main__':
    #  unittest.main()

           
# @lc code=end
