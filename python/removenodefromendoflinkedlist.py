# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        # reverse the list
        new_reverse = None
        current = head

        while current:
            next_node = current.next
            current.next = new_reverse
            new_reverse = current
            current = next_node

        # traverse logic
        current = new_reverse
        if n == 1:
            new_reverse = new_reverse.next
        else:
            while n > 2:
                current = current.next
                n -= 1
            # remove logic

            merge = current.next.next
            current.next = merge

        final = None
        current = new_reverse
        while current:
            next_node = current.next
            current.next = final
            final = current
            current = next_node
        return final
