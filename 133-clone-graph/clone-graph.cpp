class Solution {
public:
    Node* cloneGraph(Node* node) {
        unordered_map<int, Node*> clone_map;
        return dfs(node, clone_map);
    }

    Node* dfs(Node* node, unordered_map<int, Node*>& clone_map) {
        if(node == nullptr) return nullptr;
        Node* node_clone = new Node(node->val);
        clone_map[node->val] = node_clone;
        for(Node* node_child: node->neighbors){
            if(!clone_map.contains(node_child->val)){
                node_clone->neighbors.push_back(dfs(node_child, clone_map));
            } else {
                node_clone->neighbors.push_back(clone_map[node_child->val]);
            }
        }
        return node_clone;
    }
};