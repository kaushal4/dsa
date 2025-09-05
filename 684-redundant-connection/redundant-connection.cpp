class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int max_node = 0;
        unordered_set<int> visited;
        for(const auto& edge:edges){
            max_node = max(max_node, edge[0]);
            max_node = max(max_node, edge[1]);
        }

        vector<vector<int>> graph(max_node + 1, vector<int>());
        for(const auto& edge:edges){
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        vector<int> parent(max_node+1, -1);
        int u = -1;
        int v = -1;
        dfs(graph, visited, parent, 1, -1, &u, &v);

        const auto pair_hash = [](const pair<int, int> p) {
            return hash<int>{}(p.first) ^ hash<int>{}(p.second);
        };
        unordered_set<pair<int, int>, decltype(pair_hash)> cycle_nodes;
        int head = u;
        while(head != v){
            cycle_nodes.insert({head, parent[head]});
            cycle_nodes.insert({parent[head], head});
            head = parent[head];
        }
        cycle_nodes.insert({u, v});
        cycle_nodes.insert({v, u});

        reverse(edges.begin(), edges.end());
        
        for(const auto& edge: edges){
            if(cycle_nodes.contains({edge[0], edge[1]})){
                return vector<int> {edge[0], edge[1]};
            }
        }
        return vector<int>();
    }

    void dfs(vector<vector<int>>& graph,unordered_set<int>& visited,vector<int>& p, int node, int parent, int * u, int * v) {
        if(*u != -1) return; 
        if(visited.contains(node)){
            *v = node;
            return;
        }
        visited.insert(node);
        p[node] = parent;
        for(int child_node: graph[node]){
            if(child_node == parent) continue;
            dfs(graph, visited,p, child_node, node, u, v);
            if(*v != -1 && *u == -1){
                *u = node;
                return;
            }
        }
    }
};