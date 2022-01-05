# PROBLEM STATEMENT
# https://leetcode.com/problems/merge-two-sorted-lists/submissions/
# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeTwoLists1(l1, l2)

    # Time Complexity: O(n + m) where n and m are the sizes of list1 and list2
    # Space Complexity: O(1)
    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2
        else:
            p1 = list1 if list1.val <= list2.val else list2
            p2 = list1 if list1.val > list2.val else list2

            new_head = new_p = p1
            p1 = p1.next

            while p1 and p2:
                if p1.val <= p2.val:
                    new_p.next = p1
                    p1 = p1.next
                else:
                    new_p.next = p2
                    p2 = p2.next
                new_p = new_p.next

            new_p.next = p1 if p1 else p2
            return new_head