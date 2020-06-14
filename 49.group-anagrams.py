#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (55.91%)
# Likes:    3399
# Dislikes: 177
# Total Accepted:    666.4K
# Total Submissions: 1.2M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#

# @lc code=start
from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #  if len(strs) == 0:
        #      return
        #  counts = [Counter(s) for s in strs]
        #  res = []
        #  res.append([strs[0]])

        for i in 
        d = defaultdict(list)
        for s in strs:
            d["".join(sorted(s))].append(s)
        return d.values()

        
# @lc code=end
