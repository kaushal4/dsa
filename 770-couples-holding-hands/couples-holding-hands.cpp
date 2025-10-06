class Solution {
public:
    int minSwapsCouples(vector<int>& row) {
        int l = row.size();
        int n = l/2;
        unordered_map<int, unordered_set<int>> adj;
        unordered_map<int, int> edge_count;
        unordered_map<int, int> item_pos;
        for(int i = 0; i < l; i++){
            item_pos[row[i]] = i/2;
        }
        for(int i = 0; i < l; i++){
            int cur_item = row[i];
            int base_node = item_pos[cur_item];
            int parter_node = 0;
            if(cur_item%2 == 0){
                parter_node = item_pos[cur_item + 1];
            } else {
                parter_node = item_pos[cur_item - 1];
            }
            if(base_node == parter_node) continue;
            if(adj[base_node].contains(parter_node)) continue;
            adj[base_node].insert(parter_node);
            adj[parter_node].insert(base_node);
            edge_count[base_node]++;
            edge_count[parter_node]++;
        }
        int total_edges = 0;
        for(const auto&[item, count]: edge_count){
            total_edges += count;
        }
        total_edges = total_edges/2;
        queue<int> q;
        vector<int> parent(n, -2);
        int cycle_count = 0;
        for(int i = 0; i < n; i++){
            if(parent[i] != -2) continue;
            parent[i] = -1;
            q.push(i);
            while(!q.empty()){
                int node = q.front();q.pop();
                for(int child: adj[node]){
                    if(parent[child] != -2 && parent[node] != child){
                        cycle_count++;
                    } 
                    if(parent[child] == -2) {
                        parent[child] = node;
                        q.push(child);
                    }
                }
            }
        }
        cycle_count = cycle_count/2;
        return total_edges - cycle_count;
    }
};