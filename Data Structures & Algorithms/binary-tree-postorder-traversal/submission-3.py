# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)]
        # we keep track of a visited flag to track wehther
        # we've already processed a node's children. 
        # on the first visit, we set visited=True
        # then push its children
        # on the second visit, if flag visited=True, we know both children has been
        # processed, so we add the val to the result
        res = []

        while stack:
            curr, visited = stack.pop()
            if curr:
                if visited:
                    res.append(curr.val)
                else:
                    stack.append((curr, True))
                    stack.append((curr.right, False))
                    stack.append((curr.left, False))

        return res