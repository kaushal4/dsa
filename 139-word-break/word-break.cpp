class Solution {
public:
    bool check(const string& s, const string& word, const int end_index){
        int word_length = word.size();
        if(word_length > end_index + 1) return false;
        if(s.substr(end_index + 1 - word_length, word_length) == word) return true;
        return false;
    }

    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();
        vector<int> dp(n, false);

        for(int i = 0; i < n; i++){
            for(string word: wordDict){
                if(check(s, word, i)) {
                    int word_len = static_cast<int>(word.size());
                    if(i - word_len < 0){
                        dp[i] = true;
                        break;
                    } else{
                        dp[i] = dp[i] || dp[i - word_len];
                        if(dp[i]) break;
                    }
                }
            }
        }
        return dp[n-1];
    }
};