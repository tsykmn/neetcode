# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # pseudocode (brute force)
        # make a stack that keeps track of the nodes
        # transverse through all nodes in the tree
        # add it to the stack
        # sort the stack
        # return the corresponding node in k-1 index

        stack = []

        def dfs(node):
            if not node:
                return

            stack.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        stack.sort()
        return stack[k-1]

        