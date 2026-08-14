# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(tree, low, high):
            # base case: empty tree
            if not tree:
                return True
                
            # compare if within the rules of BST
            if not (low < tree.val < high):
                return False

            left = dfs(tree.left, low, tree.val)
            right = dfs(tree.right, tree.val, high)

            return left and right
            
        return dfs(root, float("-inf"), float("inf"))
        