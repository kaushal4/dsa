class Solution {
public:
    int minMaxWeight(int n, vector<vector<int>>& edges, int threshold) {
        unordered_map<int, vector<pair<int, int>>> adj;
        for (auto edge: edges) {
            adj[edge[1]].push_back(make_pair(edge[0], edge[2]));
        }

        auto cmp = [](pair<int, int> a, pair<int, int> b) { return a.second > b.second; };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> pq(cmp);
        pq.push(make_pair(0, 0));

        unordered_set<int> visited;

        int sol = 0;

        while (pq.size() > 0) {
            int node, weight;
            tie(node, weight) = pq.top(); pq.pop();

            if (visited.find(node) != visited.end()) {
                continue;
            }
            visited.insert(node);
            sol = max(sol, weight);

            for (auto child_edge :adj[node]){
                int child, edge_weight;
                tie(child, edge_weight) = child_edge;
                pq.push(make_pair(child, edge_weight));
            }
        }

        if (visited.size() < n) {
            return -1;
        }

        return sol;
    }
};