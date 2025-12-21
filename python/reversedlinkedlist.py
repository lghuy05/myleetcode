from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev


# 🧪 PROPER TESTING SETUP
def create_linked_list(arr):
    """Helper to create linked list from array"""
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    """Helper to print linked list"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    print(" -> ".join(map(str, result)) + " -> None")


sol = Solution()

# Test Case 1: Normal case
print("Test 1:")
head1 = create_linked_list([1, 2, 3, 4])
print("Original: ", end="")
print_linked_list(head1)
reversed1 = sol.reverseList(head1)
print("Reversed: ", end="")
print_linked_list(reversed1)
print()

# Test Case 2: Empty list
print("Test 2:")
head2 = create_linked_list([])
print("Original: ", end="")
print_linked_list(head2)
reversed2 = sol.reverseList(head2)
print("Reversed: ", end="")
print_linked_list(reversed2)
print()

# Test Case 3: Single element
print("Test 3:")
head3 = create_linked_list([5])
print("Original: ", end="")
print_linked_list(head3)
reversed3 = sol.reverseList(head3)
print("Reversed: ", end="")
print_linked_list(reversed3)
print_linked_list(reversed3)
print_linked_list(reversed3)
