class Solution {
public:
    std::vector<int> avoidFlood(std::vector<int>& rains) {
        int n = rains.size();
        std::vector<int> ans(n, -1);
        std::unordered_map<int, int> rains_on; 
        std::set<int> dry_days;

        for (int i = 0; i < n; ++i) {
            if (rains[i] > 0) {
                int lake = rains[i];
                if (rains_on.count(lake)) {
                    auto it = dry_days.lower_bound(rains_on[lake]);

                    if (it == dry_days.end()) {
                        return {};
                    }

                    int dry_day_idx = *it;
                    ans[dry_day_idx] = lake;
                    
                    dry_days.erase(it);
                }
                rains_on[lake] = i;
            } else { 
                dry_days.insert(i);
            }
        }

        for (int idx : dry_days) {
            ans[idx] = 1;
        }

        return ans;
    }
};