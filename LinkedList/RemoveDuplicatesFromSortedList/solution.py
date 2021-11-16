# PROBLEM STATEMENT
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.deleteDuplicatesRecursive(head)

    def deleteDuplicatesIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        else:
            previous = head
            current = head.next

            while current:
                if current.val == previous.val:
                    previous.next = current.next
                else:
                    previous = current
                current = current.next

            return head

    def deleteDuplicatesRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(current: Optional[ListNode], previous: Optional[ListNode]) -> Optional[ListNode]:
            if not current:
                return current
            else:
                if current.val != previous.val:
                    current.next = helper(current.next, current)
                    return current
                else:
                    previous.next = helper(current.next, previous)
                    return previous.next

        if not head or not head.next:
            return head
        else:
            head.next = helper(head.next, head)
            return head