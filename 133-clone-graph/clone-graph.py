class Solution:
    def __init__(self):
        self.visited:Dict[int, 'Node'] = dict()
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        if node.val in self.visited:
            return self.visited[node.val]
        node_clone = Node(node.val)
        self.visited[node.val] = node_clone
        for neighbour in node.neighbors:
            neighbour_clone = self.cloneGraph(neighbour)
            node_clone.neighbors.append(neighbour_clone)
        return node_clone