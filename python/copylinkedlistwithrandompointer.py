class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        hash_map = {}
        current = head
        while current:
            hash_map[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            copied_node = hash_map[current]

            if current.next:
                copied_node.next = hash_map[current.next]
            if current.random:
                copied_node.random = hash_map[current.random]
            current = current.next

        return hash_map[head]
