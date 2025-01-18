class Solution {
public:
    int maxRemovals(string source, string pattern, vector<int>& targetIndices) {
        int n = source.size();
        int m = pattern.size();
        unordered_set<int> s;
        for(auto indices : targetIndices) {
            s.insert(indices);
        }
        vector<vector<int>> dp(n+1, vector<int>(m+1, n));
        for(int i = 0; i < n+1 ; i++) {
            dp[i][0] = 0;
        }
        for (int i = 1; i < n+1; i++) {
            for(int j = 1; j < m+1; j++) {
                dp[i][j] = min(dp[i][j], dp[i-1][j]);
                if(source[i-1] == pattern[j-1]) {
                    if(s.find(i-1) != s.end()) {
                        dp[i][j] = min(dp[i][j], 1 + dp[i-1][j-1]);
                    } else {
                        dp[i][j] = min(dp[i][j], dp[i-1][j-1]);
                    }
                }
            }
        }
        int min_score = dp[n][m];
        //cout << min_score << endl;
        return (targetIndices.size() - min_score);
    }
};