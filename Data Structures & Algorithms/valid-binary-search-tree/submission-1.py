class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, min_val, max_val):
            if not node:
                return True
            
            # Check if current node violates the range
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # For left subtree: max becomes current node's value
            # For right subtree: min becomes current node's value
            return (helper(node.left, min_val, node.val) and 
                    helper(node.right, node.val, max_val))
        
        # Use None for initial min/max, and handle in the helper
        return helper(root, float('-inf'), float('inf'))