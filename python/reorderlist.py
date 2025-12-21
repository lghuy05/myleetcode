# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head

        fast = slow = head

        #get half list

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        right_halves = slow.next
        slow.next = None

        #sort that list

        new_head = None
        current = right_halves
        while current:
            next_val = current.next
            current.next = new_head
            new_head = current
            current = next_val

        first, second = head, new_head

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

