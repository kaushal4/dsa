class Node:
    def __init__(self, val=-1, next=None, prev = None):
        self.val = val
        self.next:Optional[Node] = next
        self.prev:Optional[Node] = prev

class Dll:
    def __init__(self):
        self.index_node:Dict[int, Node] = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.next_num = 0
        self.key_index = dict()
    
    def add(self, val)->bool:
        if val in self.key_index:
            return False
        new_node = Node(val, None)
        prev_end = self.tail.prev
        prev_end.next = new_node
        self.tail.prev = new_node
        new_node.next = self.tail
        new_node.prev = prev_end

        self.index_node[self.next_num] = new_node
        self.key_index[val] = self.next_num
        self.next_num += 1
        return True

    def remove(self, val)->bool:
        if val not in self.key_index:
            return False
        index = self.key_index[val]
        node = self.index_node[index]
        last_node = self.tail.prev
        if node == last_node:
            last_node.prev.next = self.tail
            self.tail.prev = last_node.prev
        else:
            self.tail.prev = last_node.prev
            last_node.prev.next = self.tail

            node.prev.next = last_node
            node.next.prev = last_node
            last_node.prev = node.prev
            last_node.next = node.next
            self.index_node[index] = last_node
            self.key_index[last_node.val] = index

        self.next_num -= 1
        self.key_index.pop(val)
        return True
    
    def getRandom(self):
        ran = random.randint(0, self.next_num-1)
        return self.index_node[ran].val
    

class RandomizedSet:

    def __init__(self):
        self.dll = Dll()

    def insert(self, val: int) -> bool:
        return self.dll.add(val)
        

    def remove(self, val: int) -> bool:
        return self.dll.remove(val)
        
    def getRandom(self) -> int:
        return self.dll.getRandom()