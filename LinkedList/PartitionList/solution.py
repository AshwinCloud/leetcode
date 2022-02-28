# PROBLEM STATEMENT
# https://leetcode.com/problems/partition-list/
# Given the head of a linked list and a value x, partition it such that
# all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        return self.partitionTwoPointers(head, x)

    # Time Complexity: O(n) where n is the size of head
    # Space Complexity: O(1)
    def partitionTwoPointers(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = beforeHead = ListNode(0)
        after = afterHead = ListNode(0)

        p = head

        while p:
            nxt = p.next
            if p.val < x:
                before.next = p
                before = p
            else:
                after.next = p
                after = p
            p = nxt

        after.next = None
        before.next = afterHead.next
        return beforeHead.next

    def printList(self, head: Optional[ListNode]) -> str:
        p = head
        s = ""
        while p:
            s += str(p.val) + " "
            p = p.next

        return s
