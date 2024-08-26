class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        stack = []
        queue = deque()

        stack.append(root)

        while stack:
            node = stack.pop()
            queue.appendleft(node.val)

            for child in node.children:
                stack.append(child)
        
        return list(queue)