# PROBLEM STATEMENT
# https://leetcode.com/problems/swap-nodes-in-pairs/
# Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.swapPairsRecursive(head)

    def swapPairsIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        else:
            p0 = p1 = head
            head = head.next

            while p1 and p1.next:
                p0.next = p2 = p1.next
                p1.next = p2.next
                p2.next = p1
                p0 = p1
                p1 = p1.next
            return head

    def swapPairsRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(head: Optional[ListNode]) -> Optional[ListNode]:
            if not head or not head.next:
                return head
            else:
                new_head = head.next
                head.next = helper(new_head.next)
                new_head.next = head
                return new_head

        return helper(head)