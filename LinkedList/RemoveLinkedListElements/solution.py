# PROBLEM STATEMENT
# https://leetcode.com/problems/remove-linked-list-elements/
# Given the head of a linked list and an integer val,
# remove all the nodes of the linked list that has Node.val == val, and return the new head.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        return self.removeElementsIterative(head, val)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def removeElementsIterative(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next

        current = head

        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head