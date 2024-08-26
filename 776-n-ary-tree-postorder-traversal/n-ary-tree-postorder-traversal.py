class Solution:
    def __init__(self) -> None:
        self.sol = []
    def posthelper(self, root:Optional['Node']):
        if root == None:
            return 
        for node in root.children:
            self.posthelper(node)
        
        self.sol.append(root.val)
        
    def postorder(self, root: 'Node') -> List[int]:
        self.posthelper(root)
        return self.sol