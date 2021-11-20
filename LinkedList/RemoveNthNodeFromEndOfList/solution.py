# PROBLEM STATEMENT
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return self.removeNthFromEndOnePass(head, n)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def removeNthFromEndTwoPass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def size(head: Optional[ListNode]) -> int:
            if not head:
                return 0
            else:
                num = 0
                current = head
                while current:
                    num += 1
                    current = current.next
                return num
    
        num_nodes = size(head)
        if num_nodes == 0 or num_nodes < n:
            return head
        elif num_nodes == n:
            return head.next
        else:
            index = num_nodes - n
            
            i = 0
            current = head
            while i < index - 1:
                current = current.next
                i += 1
            current.next = current.next.next
            
            return head

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def removeNthFromEndOnePass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next and n == 1:
            return None
        else:
            p1 = p2 = head
            i = 0
            while i < n:           
                p2 = p2.next
                i += 1
            
            if not p2:
                return head.next
            else:
                while p2.next:
                    p1 = p1.next
                    p2 = p2.next
                p1.next = p1.next.next
                return head
