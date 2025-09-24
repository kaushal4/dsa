class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        unordered_map<int, vector<int>> adjl;
        unordered_map<int, int> count;
        unordered_set<int> visited;
        for(const auto& pair: adjacentPairs){
            count[pair[0]]++;
            count[pair[1]]++;
            adjl[pair[0]].push_back(pair[1]);
            adjl[pair[1]].push_back(pair[0]);
        }
        int cur_node = INT_MIN;
        for(const auto&[key, value]: count){
            if(value == 1){
                cur_node = key;
                break;
            }
        }
        vector<int> ans;

        while(cur_node != INT_MIN){
            ans.push_back(cur_node);
            visited.insert(cur_node);
            int next_node = INT_MIN;
            for(const auto& neighbour: adjl[cur_node]){
                if(visited.contains(neighbour)) continue;
                next_node = neighbour;
            }
            cur_node = next_node;
        }
        return ans;
    }
};