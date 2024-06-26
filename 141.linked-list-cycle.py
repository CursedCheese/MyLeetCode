#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fast = head
        slow = head
        while fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
            if fast is None:
                return False
        return False
# @lc code=end

