# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root: TreeNode, top: TreeNode):
            if not root:
                return 0
            
            if root.val < top.val:
                return dfs(root.left, top) + dfs(root.right, top)
            else:
                return 1 + dfs(root.left, root) + dfs(root.right, root)

        return dfs(root, root)