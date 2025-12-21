# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # li = []
        #
        # def traverse(root):
        #     if not root:
        #         return
        #     li.append(root.val)
        #
        #     traverse(root.left)
        #     traverse(root.right)
        #
        # traverse(root)
        # li.sort()
        # return li[k - 1]
        self.count = 0
        self.result = None

        def traverse(root):
            if not root or self.result is not None:
                return
            traverse(root.left)
            self.count += 1
            if self.count == k:
                self.result = root.val

            traverse(root.right)

        traverse(root)
        return self.result
