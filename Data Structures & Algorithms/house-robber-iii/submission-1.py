# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dfs(node):
            if not node:
                return 0

            if node in memo:
                return memo[node]

            # Option 1: Rob this house
            rob_now = node.val
            if node.left:
                rob_now += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                rob_now += dfs(node.right.left) + dfs(node.right.right)
            
            # Option 2: Not rob this house
            skip_this = dfs(node.left) + dfs(node.right)

            memo[node] = max(rob_now, skip_this)

            return memo[node]

        return dfs(root)