# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        traversal = []
        def inorder(node):
            if node:
                inorder(node.left)
                traversal.append(node.val)
                inorder(node.right)

        inorder(root)
        if (traversal == sorted(traversal)) and (len(traversal) == len(set(traversal))):
            return True
        else: return False

        