# PROBLEM STATEMENT
# https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoNumbersIterative(l1, l2)

    def addTwoNumbersIterative(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_list = result_list_tail = None
        p1 = l1
        p2 = l2
        carry = 0

        while p1 or p2:
            sum_value = carry
            sum_value += p1.val if p1 else 0
            sum_value += p2.val if p2 else 0

            carry = sum_value // 10
            ones_place = sum_value % 10

            if not result_list:
                result_list = ListNode(ones_place)
                result_list_tail = result_list
            else:
                result_list_tail.next = ListNode(ones_place)
                result_list_tail = result_list_tail.next

            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        result_list_tail.next = ListNode(carry) if carry else None

        return result_list
