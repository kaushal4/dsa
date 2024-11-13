class Trie_Node:
    def __init__(self):
        self.child = [None] * 26
        self.is_end = False

class Trie_impl:
    
    def __init__(self, root: Trie_Node):
        self.root = root
    
    def insert(self, node:Trie_Node, word:str, index = 0):
        if index >= len(word):
            return

        child_index = ord(word[index]) - 97
        if node.child[child_index] == None:
            new_node:Trie_Node = Trie_Node()
            node.child[child_index] = new_node
        
        if index == len(word) - 1:
            node.child[child_index].is_end = True
            return

        self.insert(node.child[child_index], word, index+1)
    
    def search(self, node:Trie_Node, query:str, index = 0):
        if index >= len(query):
            return False

        child_index = ord(query[index]) - 97

        if node.child[child_index] == None:
            return False
        
        if index == len(query) - 1 and node.child[child_index].is_end:
            return True
        
        return self.search(node.child[child_index], query, index+1)
    
    def starts_with(self, node:Trie_Node, query:str, index = 0):
        print(query, index)
        
        if index >= len(query):
            return False

        child_index = ord(query[index]) - 97
        if node.child[child_index] == None:
            return False
        
        if index == len(query) - 1:
            return True
        
        return self.starts_with(node.child[child_index], query, index+1)


class Trie:

    def __init__(self):
        self.root:Trie_Node = Trie_Node()
        self.trie:Trie_impl = Trie_impl(self.root)
        

    def insert(self, word: str) -> None:
        self.trie.insert(self.root, word)
        

    def search(self, word: str) -> bool:
        return self.trie.search(self.root, word)
        

    def startsWith(self, prefix: str) -> bool:
        return self.trie.starts_with(self.root, prefix)