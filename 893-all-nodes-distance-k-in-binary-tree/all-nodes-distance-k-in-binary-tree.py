class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        path = []
        def get_path(root: Optional[TreeNode]) -> List[TreeNode]:
            if root == None:
                return []
            if root == target:
                return [target] 
            
            l = get_path(root.left)
            r = get_path(root.right)
            
            if l:
                l.append(root)
                return l
            if r:
                r.append(root)
                return r
            return []
        
        def get_dist(root: Optional[TreeNode], d = 0) -> List[int]:
            if root == None or d < 0:
                return []
            if d == 0:
                return [root.val]
            
            sol = []
            sol.extend(get_dist(root.left, d-1))
            sol.extend(get_dist(root.right, d-1))
            return sol
        
        def get_list(path:List[TreeNode]) -> List[int]:
            sol = []
            if k == 0: sol.append(path[0].val)
            sol.extend(get_dist(path[0].left, k-1))
            sol.extend(get_dist(path[0].right, k-1))
            prev = path[0]
            i = 2
            for node in path[1:]:
                if k-i+1 == 0: sol.append(node.val)
                if node.left == prev:
                    sol.extend(get_dist(node.right, k-i))
                else:
                    sol.extend(get_dist(node.left, k-i))
                i += 1
                prev = node
            return sol

        path = get_path(root)
        return get_list(path)