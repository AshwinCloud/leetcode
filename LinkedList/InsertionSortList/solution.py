# PROBLEM STATEMENT
# https://leetcode.com/problems/insertion-sort-list/
# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
# The steps of the insertion sort algorithm:
# Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
# It repeats until no input elements remain.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.insertionSortList1(head)

    # Time Complexity: O(n^2) worst case and O(n) best case
    # Space Complexity: O(1)
    def insertionSortList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = head, head.next

        while curr:
            if curr.val >= prev.val:
                prev, curr = curr, curr.next
            else:
                tmp = dummy
                while curr.val >= tmp.next.val:
                    tmp = tmp.next

                prev.next, tmp.next, curr.next = curr.next, curr, tmp.next
                curr = prev.next

        return dummy.next