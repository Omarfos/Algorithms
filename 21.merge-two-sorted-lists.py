#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (52.75%)
# Likes:    4050
# Dislikes: 578
# Total Accepted:    979K
# Total Submissions: 1.9M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new sorted list. The new
# list should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1 #l1 always points to smaller element
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
    #  def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #      if l1 == None:
    #          return l2
    #      if l2 == None:
    #          return l1
    #      res = ListNode()
    #      head = res

    #      while l1 and l2:
    #          if l1.val <= l2.val:
    #              head.next = l1
    #              l1 = l1.next
    #          else:
    #              head.next = l2
    #              l2 = l2.next
    #          head = head.next
    #      if l1 is not None:
    #          head.next = l1
    #      if l2 is not None:
    #          head.next = l2

    #      return res.next
        
# @lc code=end
