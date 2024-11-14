class TrieNode:
    def __init__(self):
        self.children:Dict[TrieNode] = dict()
        self.isLast = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isLast = True

    def search_word(self,node:TrieNode, word, index):
        found:bool = False
        if word[index] == '.':
            if index == len(word) - 1:
                if any([v.isLast for v in node.children.values()]):
                    return True
                return False
            for child in node.children.values():
                found = found or self.search_word(child, word, index+1)
        else:
            if index == len(word) - 1:
                if word[index] in node.children and node.children[word[index]].isLast:
                    return True
            else:
                if word[index] in node.children:
                    return self.search_word(node.children[word[index]], word, index+1)
        return found


    def search(self, word: str) -> bool:
        return self.search_word(self.root, word, 0)