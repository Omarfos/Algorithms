#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (59.53%)
# Likes:    4664
# Dislikes: 404
# Total Accepted:    520.9K
# Total Submissions: 874.7K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# 
# Example:
# 
# 
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# 
# 
# Constraint: It's guaranteed that the product of the elements of any prefix or
# suffix of the array (including the whole array) fits in a 32 bit integer.
# 
# Note: Please solve it without division and in O(n).
# 
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
# 
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force O(n^2)
        #  result = []
        #  for i in range(len(nums)):
        #      ans = 1
        #      for j in range(len(nums)):
        #          if i != j:
        #              ans *= nums[j]
        #      result.append(ans)

        # division
        #  result = []
        #  product = 1
        #  for num in nums:
        #      product *= num
        #  for num in nums:
        #      result.append(product // num)
        #  return result

        #  n = len(nums)
        #  left, right, ans = [1] * n, [1] * n, [1] * n

        #  for i in range(1,n):
        #      left[i] = left[i-1] * nums[i-1]

        #  for i in reversed(range(n-1)):
        #      right[i] = right[i+1] * nums[i+1]

        #  for i in range(n):
        #      ans[i] = right[i] * left[i]

        #  return ans

        ans = [1]
        n = len(nums)
        for i in range(1, n):
            ans.append(ans[i-1] * nums[i-1])
        # [1,2,3,4]
        # [1,1,2,6]
        R = 1
        for i in reversed(range(n)):
            ans[i] = ans[i] * R 
            R *= nums[i]
        return ans





        
# @lc code=end
