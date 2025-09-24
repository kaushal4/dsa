using pi = pair<int, int>;

const auto comp = [](const pi &a, const pi &b)
{
    return a.second > b.second;
};

class Solution {
public:
    pi findLowest(unordered_set<int>& visitedNodes,priority_queue<pi, vector<pi>, decltype(comp)>& nodeComp){
        pi ans = {-1, -1};
        while(!nodeComp.empty() && ans.first == -1){
            pi posNode = nodeComp.top(); nodeComp.pop();
            if(visitedNodes.contains(posNode.first)) continue;
            ans = posNode;
        }
        return ans;
    }

    int minTime(int n, vector<vector<int>>& edges) {
        unordered_set<int> visitedNodes;
        priority_queue<pi, vector<pi>, decltype(comp)> nodeComp(comp);
        unordered_map<int, vector<vector<int>>> adj;
        for(const auto& edge: edges){
            adj[edge[0]].push_back({edge[1], edge[2], edge[3]});
        }
        nodeComp.push({0, 0});
        int ans = -1;

        while(!nodeComp.empty()){
            pi chosenNode = findLowest(visitedNodes, nodeComp);
            int node = chosenNode.first;
            visitedNodes.insert(node);
            int time = chosenNode.second;
            if(node == -1) return -1;
            if(node == n-1){
                ans = time;
                break;
            }

            for(const auto& edge: adj[node]){
                if(edge[2] < time) continue;
                int bestTime = max(time + 1, edge[1]+1);
                if(visitedNodes.contains(edge[0])) continue;
                nodeComp.push({edge[0], bestTime});
            }
        }
        return ans;
    }
};