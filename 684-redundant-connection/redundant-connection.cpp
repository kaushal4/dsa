class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int max_node = 0;
        for (const auto &edge : edges) {
            max_node = max(max_node, max(edge[0], edge[1]));
        }
        vector<vector<int>> graph(max_node+1);
        for(const auto& edge: edges){
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        vector<int> parent(max_node+1, -1);
        queue<int> q;
        q.push(1);

        int u = -1;
        int v = -1; 
        parent[1] = 1;

        while(!q.empty() && u == -1){
            int cur_node = q.front(); q.pop();
            for(const auto& child_node: graph[cur_node]) {
                if(parent[child_node] != -1 && parent[cur_node] != child_node) {
                    u = child_node;
                    v = cur_node;
                    break;
                }
                if(parent[child_node] == -1){
                    parent[child_node] = cur_node;
                    q.push(child_node);
                }
            }
        }

        parent[1] = -1;

        vector<int> cycle_elements;
        unordered_set<int> v_elements;
        auto pair_hash = [](const pair<int, int>& p) {
            return hash<int>{}(p.first) ^ hash<int>{}(p.second);
        };
        int head = v;
        while(head != -1){
            v_elements.insert(head);
            head = parent[head];
        }
        head = u;
        while(!v_elements.contains(head)){
            head = parent[head];
        }
        int common_point = head;
        unordered_set<pair<int, int>, decltype(pair_hash)> cycle_edges;
        head = v;
        while(head != common_point){
            cycle_edges.insert({head, parent[head]});
            cycle_edges.insert({parent[head], head});
            head = parent[head];
        }
        head = u;
        while(head != common_point){
            cycle_edges.insert({head, parent[head]});
            cycle_edges.insert({parent[head], head});
            head = parent[head];
        }

        cycle_edges.insert({u, v});
        cycle_edges.insert({v, u});

        reverse(edges.begin(), edges.end());

        for(auto& edge: edges){
            pair<int, int> edge_pair = pair(edge[0], edge[1]);
            if(cycle_edges.contains(edge_pair)){return vector<int>{edge[0], edge[1]};};
        }
        return vector<int>();
    }
};