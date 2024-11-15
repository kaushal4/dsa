class Solution:
    def compare_words(self, word1:str, word2:str):
        diff_count = 0
        i = 0
        n = len(word1)
        for i in range(n):
            if word1[i] != word2[i]:
                diff_count += 1
        return diff_count

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        if endWord not in wordList:
            return 0
        adj = {word:[] for word in wordList}
        n = len(wordList)

        for i in range(n):
            for j in range(i+1, n):
                if self.compare_words(wordList[i], wordList[j]) == 1:
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        
        queue = deque()
        visited = set()
        queue.append(beginWord)
        visited.add(beginWord)
        distance = 1
        distances = {word:0 for word in wordList}

        while(queue):
            i = len(queue)
            while(i):
                node = queue.popleft()
                for child in adj[node]:
                    if child not in visited:
                        distances[child] = distance
                        visited.add(child)
                        queue.append(child)


                i-=1
            distance += 1
        return distances[endWord]+1 if distances[endWord] != 0 else 0