#
# @lc app=leetcode id=896 lang=python
#
# [896] Monotonic Array
#
# https://leetcode.com/problems/monotonic-array/description/
#
# algorithms
# Easy (57.43%)
# Likes:    588
# Dislikes: 35
# Total Accepted:    97.9K
# Total Submissions: 170.4K
# Testcase Example:  '[1,2,2,3]'
#
# An array is monotonic if it is either monotone increasing or monotone
# decreasing.
# 
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array
# A is monotone decreasing if for all i <= j, A[i] >= A[j].
# 
# Return true if and only if the given array A is monotonic.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,2,3]
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: [6,5,4,4]
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: [1,3,2]
# Output: false
# 
# 
# 
# Example 4:
# 
# 
# Input: [1,2,4,5]
# Output: true
# 
# 
# 
# Example 5:
# 
# 
# Input: [1,1,1]
# Output: true
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # increasing
        if len(A) <= 1:
            return True

        # [2, 2]
        i = 1
        while i < len(A) and A[i] == A[i-1]:
            i += 1

        if i == len(A):
            return True

        # [2, 2, 3]
        # [2, 2, 1]
        case = A[i] - A[i-1] # increasing or decreasing
        for j in range(i+1, len(A)):
            if A[j] - A[j-1] < 0 and case > 0: 
                return False
            if A[j] - A[j-1] > 0 and case < 0: 
                return False

        return True

        
# @lc code=end
