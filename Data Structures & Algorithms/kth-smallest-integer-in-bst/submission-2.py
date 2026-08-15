# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = k
        res = root.val

        def dfs(tree):
            nonlocal n, res
            if not tree:
                return

            dfs(tree.left)
            if n == 0:
                return
            
            n -= 1

            if n == 0:
                res = tree.val
                return

            dfs(tree.right)

        dfs(root)

        return res
        