from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        maxVal = 0
        MOD = 10**9 + 7

        def sumAllTree(node):
            if not node:
                return 0
            return node.val + sumAllTree(node.left) + sumAllTree(node.right)

        sumAllTree = sumAllTree(root)

        def cutEdge(node):
            if not node:
                return 0
            nonlocal maxVal
            subTree = node.val + cutEdge(node.left) + cutEdge(node.right)
            maxVal = max(maxVal, (sumAllTree - subTree) * subTree)
            return subTree

        cutEdge(root)
        return maxVal % MOD
