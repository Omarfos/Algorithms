#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (61.64%)
# Likes:    4937
# Dislikes: 261
# Total Accepted:    534.5K
# Total Submissions: 867.1K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(a, left, right, res):
            if not right:
                res.append(a)
            if left:
                backtrack(a + '(', left - 1, right, res)
            if right > left:
                backtrack(a + ')', left, right - 1, res)
        res = []
        backtrack('', n, n, res)
        return res
    #  def generateParenthesis(self, n):
    #      def generate(p, left, right, parens=[]):
    #          if left:         generate(p + '(', left-1, right)
    #          if right > left: generate(p + ')', left, right-1)
    #          if not right:    parens += p,
    #          return parens
    #      return generate('', n, n)

        
# @lc code=end
