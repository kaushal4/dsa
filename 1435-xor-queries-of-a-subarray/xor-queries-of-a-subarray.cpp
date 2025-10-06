class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        int n = arr.size();
        int m = queries.size();
        vector<int> cumulative(n+1, 0);
        int cur_xor = 0;
        for(int i = 0; i < n; i++){
            cur_xor = cur_xor ^ arr[i];
            cumulative[i+1] = cur_xor;
        }
        vector<int> ans;
        for(int i = 0; i < m;i ++){
            vector<int>& query = queries[i];
            ans.push_back(cumulative[query[1]+1] ^ cumulative[query[0]]);
        }
        return ans;
    }
};