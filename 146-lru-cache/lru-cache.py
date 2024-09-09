class LRUCache:

    class Node:
        def __init__(self, key, value, back, next) -> None:
            self.key = key
            self.value = value
            self.back = back
            self.next = next

    def __init__(self, capacity: int):
        self.header = self.Node(-1, -1, None, None)
        self.footer = self.Node(-1, -1, None, None)
        self.capacity = capacity
        self.hash = dict()
        self.size = 0
        

    def get(self, key: int) -> int:
        if key in self.hash:
            self.put(key, self.hash[key].value)
            return self.hash[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            node = self.hash[key]
            # remove node from ll
            next = node.next
            back = node.back
            back.next = next
            next.back = back
            self.size -= 1
        elif self.size == self.capacity:
            to_delete = self.footer.next
            self.hash.pop(to_delete.key)
            next = to_delete.next
            self.footer.next = next
            next.back = self.footer
            self.size -= 1

        new_node = self.Node(key, value, None, None)
        self.hash[key] = new_node
        
        if self.size == 0:
            self.header.back =  new_node
            self.footer.next = new_node
            new_node.next = self.header
            new_node.back = self.footer
        else:
            prev = self.header.back
            prev.next = new_node
            new_node.next = self.header
            self.header.back = new_node
            new_node.back = prev
        self.size += 1