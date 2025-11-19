# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        li = []

        def dfs(node, level):
            count = 0
            if not node:
                return 0
            if len(li) == level:
                if not li:
                    count = 1
                    li.append(node.val)
                else:
                    if node.val >= max(li):
                        count += 1
                    li.append(node.val)
            else:
                if node.val >= max(li[:level]):
                    count += 1
                li[level] = node.val

            left = dfs(node.left, level + 1)
            right = dfs(node.right, level + 1)
            return count + left + right

        return dfs(root, 0)
