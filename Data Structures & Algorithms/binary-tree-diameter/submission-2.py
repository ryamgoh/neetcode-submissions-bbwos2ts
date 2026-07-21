# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        def helper(node):
            nonlocal res
            if not node:
                return 0

            left_h = helper(node.left)
            right_h = helper(node.right)

            res = max(res, left_h + right_h)

            return 1 + max(left_h, right_h)



        helper(root)

        return res