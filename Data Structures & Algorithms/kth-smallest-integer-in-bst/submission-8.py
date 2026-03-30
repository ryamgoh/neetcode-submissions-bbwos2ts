# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.remaining = k
        self.result = None

        def dfs(node):
            if not node or self.result:
                return

            dfs(node.left)
            if self.remaining > 0:
                self.remaining -= 1
                if  self.remaining == 0:
                    self.result = node.val

            dfs(node.right)

        dfs(root)

        return self.result
            