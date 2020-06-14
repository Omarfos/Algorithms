#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (29.12%)
# Likes:    6883
# Dislikes: 1065
# Total Accepted:    667.7K
# Total Submissions: 2.3M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#

# @lc code=start
# Combine both arrays in sequence, then find the midpoint O(n)
# Median: A[n/2] if n is odd, otherwise it's (A[n/2] + A[n-1/2]) / 2 
# Divide and conquer strat: Is there a way to eliminate half of the search
# space?

# Example: 
#   nums1 = [1,2,3,4]
#   nums2 = [100]
# index of median is (n+m / 2) 

# Algorithm
#   if max(nums1) < min(nums2):
#       reduces to finding the median of a sorted array
#       [1,2] [3,4,5]
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        if (n + m) % 2 == 1:
            target_index = (n + m) // 2

        i = n - 1
        pivot = nums1[i]
        while:
            j = binary_search(nums2, pivot)
            # todo, add even arrays
            if i + j + 1 == target_index:
                return nums1[j]


    def binary_search(A, num):
        if 
        pass

        
# @lc code=end
