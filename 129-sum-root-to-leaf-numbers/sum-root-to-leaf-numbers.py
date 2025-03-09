class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def recur(root:Optional[TreeNode], cur_no):
            if root == None:
                return 0
            sol = 0
            new_no = (cur_no * 10) + root.val
            if root.left == None and root.right == None:
                return new_no
            sol += recur(root.left, new_no)
            sol += recur(root.right, new_no)
            
            return sol
        return recur(root, 0)