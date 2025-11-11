# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        n = 0
        current = head
        while current:
            n += 1
            current = current.next

        dummy = ListNode(0)
        tail = dummy
        while n >= k:
            prev = None
            current = head
            k_head = current
            for _ in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            tail.next = prev
            tail = k_head
            n -= k
        if current:
            tail.next = current

        return dummy.next
