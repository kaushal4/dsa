class Solution {
public:
    long long beautifulSubarrays(vector<int>& nums) {
        long long ans = 0;
        unordered_map<int, int> cur;
        cur[0] = 1;
        int cur_num = 0;
        for(const auto& num: nums){
            cur_num = cur_num ^ num;
            //cout<<cur_num<<" "<<cur[cur_num]<<endl;
            ans += cur[cur_num];
            cur[cur_num] += 1;
        }
        return ans;
    }
};