class Solution {
public:
    bool isPossible(string s) {
        int n = s.size();
        if(n > 1 && s[0] == '0') {
            return 0;
        }
        int num = stoi(s);
        return 1 <= num && num <=26;
    }

    int recur(vector<int>& dp,const string& s, const int pos){
        if(pos < 0) return 0;
        if(dp[pos] != -1) return dp[pos];
        dp[pos] = (isPossible(string(1, s[pos]))?recur(dp, s, pos-1):0) + (isPossible(s.substr(pos-1, 2))?recur(dp, s, pos-2):0);
        return dp[pos];
    }

    int numDecodings(string s) {
        int n = s.size();
        vector<int> dp(n, -1);
        dp[0] = isPossible(string(1,s[0]));
        if(n == 1) return dp[0];
        dp[1] = isPossible(s.substr(0, 2)) + (isPossible(string(1,s[1]))?dp[0]:0); 
        return recur(dp, s, n-1);
    }
};