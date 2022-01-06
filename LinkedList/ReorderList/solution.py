# PROBLEM STATEMENT
# https://leetcode.com/problems/reorder-list/
# You are given the head of a singly linked-list. The list can be represented as:
# Reorder the list to be on the following form:
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        return self.reorderList1(head)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reorderList1(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        else:
            slow_p = head
            fast_p = head.next

            while fast_p and fast_p.next:
                fast_p = fast_p.next.next
                slow_p = slow_p.next

            if fast_p:
                slow_p = slow_p.next

            reversed_list = self.reverseList(slow_p)

            p1 = head
            p2 = reversed_list

            while p2 and p2.next:
                p1.next, p1.next.next, p1, p2 = p2, p1.next, p1.next, p2.next

            return head

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            curr.next, curr, prev = prev, curr.next, curr

        return prev

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def listToString(self, head: Optional[ListNode]) -> Optional[ListNode]:
        string = "["

        while head:
            string += " " + str(head.val) + " "
            head = head.next

        string += "]"

        return string