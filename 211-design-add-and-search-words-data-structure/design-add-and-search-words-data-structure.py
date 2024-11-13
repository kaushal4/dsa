class TrieNode:
    def __init__(self, val):
        self.children:Set[TrieNode] = set()
        self.val = val
        self.isLast = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode(-1)

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            found:bool = False
            for child in node.children:
                if child.val == c:
                    found = True
                    node = child
                    break
            if not found:
                new_node = TrieNode(c)
                node.children.add(new_node)
                node = new_node
        node.isLast = True

    def search_word(self,node:TrieNode, word, index):
        found:bool = False
        if word[index] == '.':
            if index == len(word) - 1:
                for child in node.children:
                    if child.isLast:
                        return True
                return False
            for child in node.children:
                found = found or self.search_word(child, word, index+1)
        else:
            if index == len(word) - 1:
                for child in node.children:
                    if child.val == word[index] and child.isLast:
                        return True
            else:
                for child in node.children:
                    if child.val == word[index]:
                        found = self.search_word(child, word, index+1)
        return found


    def search(self, word: str) -> bool:
        return self.search_word(self.root, word, 0)