class Solution {
public:
    vector<vector<int>> reconstructMatrix(int upper, int lower, vector<int>& colsum) {
        int num_two = 0;
        int n = colsum.size();
        vector<vector<int>> ans(2, vector<int> (n, 0));
        int i = 0;
        for(const auto& cols: colsum){
            if(cols == 1){
                if(upper == 0 && lower == 0) return vector<vector<int>>();
                if(upper > lower){
                    ans[0][i] = 1; upper -= 1;
                } else {
                    ans[1][i] = 1; lower -= 1;
                }
            }
            if(cols == 2){
                if(upper == 0 || lower == 0) return vector<vector<int>>();
                ans[0][i] = 1; upper -= 1;
                ans[1][i] = 1; lower -= 1;
            }
            i += 1;
        }
        if(upper != 0  || lower != 0) return vector<vector<int>>();
        return ans;
    }
};