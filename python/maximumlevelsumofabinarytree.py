# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxlevelsum(self, root: Optional[treenode]) -> int:
        def bfs(root):
            max_sum = float("-inf")
            if not root:
                return 1
            queue = deque([root])
            max_level = 1
            current_level = 1
            while queue:
                current_sum = 0
                n = len(queue)
                for i in range(n):
                    current_node = queue.popleft()
                    current_sum += current_node.val
                    if current_node.left:
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)
                if current_sum > max_sum:
                    max_level = current_level
                    max_sum = current_sum
                current_level += 1
            return max_level

        max_level = bfs(root)
        return max_level
