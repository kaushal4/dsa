class Solution {
public:
    int minSol(int num) {
        int sol = -1;
        for(int i = num - 1; i >= 0; i--){
            if ((i | i+1) == num) {
                sol = i;
            }
        }
        return sol;
    }
    vector<int> minBitwiseArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, INT_MAX);
        for(int i = 0; i < n; i++){
            ans[i] = minSol(nums[i]);
        }
        return ans;
    }
};