class Solution {
public:
    vector<int> rearrangeBarcodes(vector<int>& barcodes) {
        unordered_map<int, int> count;
        vector<int> sol;
        for(const auto& bar: barcodes){
            count[bar] += 1;
        }
        const auto comp = [](pair<int, int> a, pair<int, int> b){
            return a.second < b.second;
        };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(comp)> pq(comp);
        for(const auto& [key, value] : count){
            pq.push({key, value});
        }
        while(pq.size() > 1){
            pair<int, int> high = pq.top();pq.pop();
            pair<int, int> low = pq.top(); pq.pop();

            sol.push_back(high.first);
            sol.push_back(low.first);
            if(high.second > 1) pq.push({high.first, high.second - 1});
            if(low.second > 1) pq.push({low.first, low.second - 1});
        }
        if(!pq.empty()){
            pair<int, int> high = pq.top();pq.pop();
            sol.push_back(high.first);
            if(high.second > 1) pq.push({high.first, high.second - 1});
        }
        return sol;
    }
};