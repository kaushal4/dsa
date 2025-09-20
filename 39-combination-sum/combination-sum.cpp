class Solution {
public:

    void recur(vector<int>& candidates,vector<int>& cur_numbers, vector<vector<int>>& sol, int target, int cur, int cur_sum){
        int n = candidates.size();
        cout<<cur_sum<<endl;
        if(cur_sum == target) {
            sol.push_back(vector<int>(cur_numbers));
            return;
        }
        if(cur >= n) return;
        int candidate = candidates[cur];

        int i = 0;
        while((cur_sum + candidate * i) <= target){
            if(i!=0)cur_numbers.push_back(candidate);
            recur(candidates, cur_numbers, sol, target, cur+1, cur_sum + (candidate * i));
            i+=1;
        }
        i -= 1;
        while(i > 0){
            cur_numbers.pop_back();
            i -= 1;
        }
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> cur_numbers;
        int cur_sum = 0;
        recur(candidates, cur_numbers, ans, target, 0, cur_sum);
        return ans;
    }
};