# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def helper(node, p, q):
            if not node:
                return None
            if p.val > node.val and q.val > node.val and node.right:
                return helper (node.right, p, q)
            elif p.val < node.val and q.val < node.val and node.left:
                return helper (node.left, p, q)
            else:
                return node

        return helper(root, p, q)
