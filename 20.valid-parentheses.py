#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (38.64%)
# Likes:    4869
# Dislikes: 214
# Total Accepted:    986.8K
# Total Submissions: 2.6M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(':')', '{':'}', '[':']'}
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            else: #closing bracket
                if not stack:
                    return False
                open_bracket = stack.pop()
                if bracket != pairs[open_bracket]:
                    return False

        return len(stack) == 0

#  import unittest

#  class TestSolution(unittest.TestCase):
#      def setUp(self):
#          self.solution = Solution()
#      def test_one(self):
#          r = self.solution.isValid('()')
#          self.assertEqual(r,True)


#  if __name__ == '__main__':
#      unittest.main()

           
        
# @lc code=end
