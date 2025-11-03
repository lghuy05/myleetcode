# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash = set()
        current = head

        while current:
            if current not in hash:
                hash.add(current)
                current = current.next
            else:
                return True
        return False
