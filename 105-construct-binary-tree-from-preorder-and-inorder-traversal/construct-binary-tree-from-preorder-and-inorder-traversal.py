class Solution:
    def build(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        if preorder[0] not in inorder:
            return None

        inorder_index = inorder.index(preorder[0])
        root_node = TreeNode(preorder[0],None, None)
        root_node.left = self.build(preorder[1:inorder_index+1],inorder[:inorder_index])
        root_node.right = self.build(preorder[inorder_index+1:],inorder[inorder_index+1:])
        return root_node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, inorder)