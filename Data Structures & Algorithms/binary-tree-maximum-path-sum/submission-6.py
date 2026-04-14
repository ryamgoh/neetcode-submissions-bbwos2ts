# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize with the smallest possible value
        total = float('-inf')

        def dfs(node):
            nonlocal total
            if not node:
                return 0
            
            # Get max path sum from left and right subtrees (ignore negative paths)
            val_left = max(dfs(node.left), 0)
            val_right = max(dfs(node.right), 0)
            
            # Current path sum if we split at this node
            current_path_sum = node.val + val_left + val_right
            
            # Update global maximum
            total = max(total, current_path_sum)
            
            # Return the max path sum without splitting
            # (the path that continues to parent must be a straight line)
            return node.val + max(val_left, val_right)
        
        dfs(root)
        return int(total)