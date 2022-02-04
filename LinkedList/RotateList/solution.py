# PROBLEM STATEMENT
# https://leetcode.com/problems/rotate-list/
# Given the head of a linked list, rotate the list to the right by k places.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return self.rotateRightSize(head, k)

    # Time Complexity: O(n) where n is the size of head
    # Space Complexity: O(1)
    def rotateRightSize(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        else:
            p = head
            size = 0
            while p:
                p = p.next
                size += 1

            if k % size:
                p1 = p2 = head
                for _ in range(k % size):
                    p2 = p2.next

                while p2.next:
                    p1 = p1.next
                    p2 = p2.next

                p2.next = head
                head = p1.next
                p1.next = None

            return head