class Solution {
public:
    bool canFit(vector<int>& piles,int h, int val){
        if(val < 1) return false;
        long long cycles_required = 0;
        for(const auto& pile: piles){
            cycles_required += ceil((double)pile/ val);
        }
        return cycles_required <= h;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        int best_freq = -1;
        int min_freq = 1;
        int max_freq = *max_element(piles.begin(), piles.end());
        while(min_freq <= max_freq){
            int mid = min_freq + (max_freq - min_freq)/2;
            if(canFit(piles, h, mid)){
                best_freq = mid;
                max_freq = mid - 1;
            } else {
                min_freq = mid + 1;
            }
        }
        return best_freq;
    }
};