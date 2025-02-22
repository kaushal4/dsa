class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return -1
        best_seen = root.val
        def recur(root: Optional[TreeNode]) -> int:
            nonlocal best_seen
            if root == None:
                return 0
            
            best_left = recur(root.left)
            best_right = recur(root.right)
            
            best_val = max([root.val, root.val + best_left, root.val + best_right])
            best_seen = max(best_seen, best_val, root.val + best_left + best_right)
            return best_val
        recur(root)
        return best_seen