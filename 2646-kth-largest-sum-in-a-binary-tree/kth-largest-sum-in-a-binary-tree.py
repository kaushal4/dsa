class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque()
        q.append(root)
        sums = []

        while q:
            level_len = len(q)
            level_sum = 0
            while level_len:
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level_len -= 1
            sums.append(level_sum)
        sums.sort(reverse=True)
        if len(sums) < k:
            return -1
        return sums[k-1]