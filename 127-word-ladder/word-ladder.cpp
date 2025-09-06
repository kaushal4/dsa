class Solution {
public:
    bool isOneDiff(string word1, string word2) {
        int n = word1.size();
        if(n != word2.size()) return false;
        
        int diff = 0;

        for(int i = 0;i < n && diff <=1; i++){
            if(word1[i] != word2[i]) diff += 1;
        }

        return diff == 1?true:false;
    }

    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        int n = wordList.size();
        bool end_found = false;
        unordered_map<string, vector<string>> graph;
        for(int i = 0;i < n; i++){
            if(wordList[i] == endWord) end_found = true;
            for(int j = i+1; j < n; j++){
                if(isOneDiff(wordList[i],wordList[j])){
                    graph[wordList[i]].push_back(wordList[j]);
                    graph[wordList[j]].push_back(wordList[i]);
                }
            }
        }
        for (int j = 0; j < n; j++)
        {
            if (isOneDiff(beginWord, wordList[j]))
            {
                graph[beginWord].push_back(wordList[j]);
                graph[wordList[j]].push_back(beginWord);
            }
        }

        if (!end_found)
            return 0;

        queue<string> q({beginWord});
        unordered_set<string> visited;
        visited.insert(beginWord);
        int ans = 0;
        while (!q.empty())
        {
            ans += 1;
            int cur_queue_size = q.size();
            while (cur_queue_size--)
            {
                string cur_word = q.front();
                q.pop();
                for (const auto &child_word : graph[cur_word])
                {
                    if (child_word == endWord)
                        return ans+1;
                    if (!visited.contains(child_word))
                    {
                        visited.insert(child_word);
                        q.push(child_word);
                    }
                }
            }
        }

        return 0;
    }
};