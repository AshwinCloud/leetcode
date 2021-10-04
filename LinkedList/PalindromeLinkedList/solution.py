# Given the head of a singly linked list, return true if it is a palindrome.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        return self.isPalindromeStack(head)
    
    def isPalindromeStack(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        else:
            stack = []
            slow = head
            fast = head
            
            while fast and fast.next:
                stack.append(slow.val)
                print("slow: ", slow.val, "fast: ", fast.val)
                slow = slow.next
                fast = fast.next.next
            
            if fast:
                slow = slow.next

            while stack:
                if stack.pop() != slow.val:
                    return False
                slow = slow.next
            
            return True