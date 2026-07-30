# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def helper(node, maxVal):
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0
            res += helper(node.left, max(node.val, maxVal))
            res += helper(node.right, max(node.val, maxVal))
            return res

        goodnodes = helper(root, root.val)
        return goodnodes
        