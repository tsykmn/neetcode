# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        def inOrder(tree):
            if not tree:
                return

            inOrder(tree.left)
            stack.append(tree.val)
            inOrder(tree.right)

        inOrder(root)

        return stack[k-1]