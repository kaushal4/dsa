class Solution {
public:
    long long minTime(vector<int>& skill, vector<int>& mana) {
        using uint = __uint128_t;
        uint n = skill.size();
        uint m = mana.size();
        vector<uint> end_times(n,0);
        vector<uint> start_time_arr(n, 0);

        for(uint i= 0; i < m; i++){
            uint max_before_time = 0;
            for(uint j = 0; j < n; j++){
                uint start_time = 0;
                if(max_before_time >= end_times[j]){
                    start_time = max_before_time;
                } else {
                    start_time = end_times[j];
                }
                uint new_time = start_time + (skill[j] * mana[i]);
                end_times[j] = new_time;
                max_before_time = new_time;
            }
            for(uint j = n-1; j >= 1; j--){
                end_times[j-1] = max(end_times[j-1], end_times[j] - (skill[j] * mana[i]));
            }
        }
        return end_times[n-1];
    }
};