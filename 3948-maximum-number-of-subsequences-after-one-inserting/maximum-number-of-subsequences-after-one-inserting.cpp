class Solution {
public:
    long long numOfSubsequences(string s) {
        long long ans = 0;
        int n = s.size();
        vector<int> sCount(n, 0);
        int TCount = 0;
        int lCount = 0;
        long long lcCount = 0;
        for(int i = 0; i < n; i++) {
            if(s[i] == 'L'){
                lCount += 1;
            } 
            if(s[i] == 'C'){
                lcCount += lCount;
            } 
            if(s[i] == 'T') {
                ans = ans + (lcCount);
            }
            sCount[i] = lCount;
        }

        long long possibleIncrease = 0;
        long long ctCount = 0;

        for(int i = n-1; i > -1; i--){
            if(s[i] == 'T') TCount += 1;
            int LCount = sCount[i];
            possibleIncrease = max(possibleIncrease, (long long)TCount * LCount);
            if(s[i] == 'C'){
                ctCount += TCount;
            }
        }

        ans = max(ans + ctCount, max(ans + lcCount, ans + possibleIncrease));
        return ans;
    }
};