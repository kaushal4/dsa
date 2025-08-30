struct sol {
    int size;
    int i;
    int j;

    sol(const int size, const int i, const int j): size(size), i(i), j(j) {}

    auto operator<=>(const sol& other) const {
        return size <=> other.size;
    }

    bool operator==(const sol& other) const {
        return size == other.size;
    }
};

class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        sol ans = sol(1,0,0);

        vector<vector<bool>> dp(n, vector<bool> (n, true));

        for(int i = n-2; i >= 0; i--){
            for(int j = n-1; j>i ; j--){
                dp[i][j] = s[i] == s[j] && dp[i+1][j-1];
                if(dp[i][j]){
                    ans = max(ans, sol(j-i+1, i, j));
                }
            }
        }
        return s.substr(ans.i, ans.size);
    }
};