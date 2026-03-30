# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root: TreeNode, top: TreeNode):
            
            # Base case: empty subtree has no good nodes
            if not root:
                return 0
            
            # If current node's value is less than the maximum seen so far
            # This node is NOT good (since it's smaller than a previous node)
            if root.val < top.val:
                # Don't count current node, but continue checking children
                # Children are still evaluated against the same maximum (top)
                return dfs(root.left, top) + dfs(root.right, top)
            
            # If current node's value is greater than OR EQUAL TO the maximum seen so far
            # This node IS good (it's either new maximum or ties with current maximum)
            else:
                # Count this node (1) plus good nodes in left and right subtrees
                # For children, this node becomes the new maximum to beat
                return 1 + dfs(root.left, root) + dfs(root.right, root)

        # Start the DFS from the root, with the root itself as the initial maximum
        return dfs(root, root)