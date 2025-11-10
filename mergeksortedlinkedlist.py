# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        li = []
        for i in lists:
            # each linked list
            current = i
            while current:
                li.append(current.val)
                current = current.next
        li.sort()

        dummy = ListNode(0)
        current = dummy
        for i in li:
            current.next = ListNode(i)
            current = current.next
        return dummy.next
