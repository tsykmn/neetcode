# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(tree):
            nonlocal res
            if not tree:
                return 0

            leftMax = dfs(tree.left)
            rightMax = dfs(tree.right)

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res = max(res, tree.val + leftMax + rightMax)
            return tree.val + max(leftMax, rightMax)

        dfs(root)
        return res
        