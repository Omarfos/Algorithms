#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (33.43%)
# Likes:    8067
# Dislikes: 2057
# Total Accepted:    1.4M
# Total Submissions: 4.1M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#  Go through each Linked List, convert it to an int, then add both
#  Do it in place, no need to traverse everything

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = sent = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            rval = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) // 10
            r.next = ListNode(rval)
            r = r.next
        return sent.next

        #  a = self.node_to_int(l1)
        #  b = self.node_to_int(l2)
        #  s = str(a + b) # 807
        #  r = ListNode(int(s[0])) # 8
        #  for i in s[1:]:
            #  l = ListNode(int(i))
            #  l.next = r
            #  r = l
        #  return r
            
    def node_to_int(self, l: ListNode):
        r, base = 0, 1
        while l:
            r += l.val * base
            base *= 10
            l = l.next
        return r
        
# @lc code=end
