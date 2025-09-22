class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int low = 0;
        int high = 0;
        int n = fruits.size();
        vector<vector<int>> s(2, vector<int> {-1,-1});
        s[0][0] = fruits[low];
        s[0][1] = 0;
        int ans = 1;

        while(high < n-1){
            if(fruits[high + 1] == s[0][0] || fruits[high+1] == s[1][0]){
                if(fruits[high + 1] == s[0][0]) s[0][1] = high + 1;
                else if(fruits[high + 1] == s[1][0]) s[1][1] = high + 1;
                high += 1;
            } else if(s[0][0] == -1 || s[1][0] == -1) {
                if(-1 == s[0][0]) {
                    s[0][1] = high + 1;
                    s[0][0] = fruits[high + 1];
                } 
                else if(-1 == s[1][0]) {
                    s[1][1] = high + 1;
                    s[1][0] = fruits[high + 1];
                }
                high += 1;
            } else {
                if(s[0][0] == fruits[low] && s[0][1] == low){
                    s[0][0] = -1;
                    s[0][1] = -1;
                } else if(s[1][0] == fruits[low] && s[1][1] == low){
                    s[1][0] = -1;
                    s[1][1] = -1;
                }
                low += 1;
            }
            ans = max(ans, high - low + 1);
        }
        return ans;
    }
};