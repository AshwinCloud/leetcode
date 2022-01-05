# PROBLEM STATEMENT
# https://leetcode.com/problems/merge-k-sorted-lists/
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.mergeKLists1(lists)

    # Time Complexity: O(n log k) where n is the total size of the all the lists combined and k is the number of lists
    # Space Complexity: O(1)
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            while len(lists) > 1:
                intermediate_lists = []

                for i in range(0, len(lists), 2):
                    list1 = lists[i]
                    list2 = lists[i + 1] if i < len(lists) - 1 else None

                    merged_list = self.merge2Lists1(list1, list2)

                    intermediate_lists.append(merged_list)

                lists = intermediate_lists

            return lists[0]

    # Time Complexity: O(n) where n is the total size of list1 and list2 combined
    # Space Complexity: O(1)
    def merge2Lists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2
        else:
            p1, p2 = (list1, list2) if list1.val < list2.val else (list2, list1)
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

