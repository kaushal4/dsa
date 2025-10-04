class Solution {
public:
    TreeNode* sol;
    TreeNode* findCommon(TreeNode* root, int max_dept, int cur_depth){
        if(root == nullptr) return nullptr;
        if(max_dept == cur_depth){
            sol = root;
            return root;
        }
        TreeNode* left = findCommon(root->left, max_dept, cur_depth + 1);
        TreeNode* right = findCommon(root->right, max_dept, cur_depth + 1);
        if(left != nullptr && right != nullptr){
            sol = root;
        }
        if(left!= nullptr || right != nullptr){
            return root;
        }
        return nullptr;
    }

    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        int level = -1;
        while(!q.empty()){
            int level_len = q.size();
            level ++;
            while(level_len--){
                TreeNode* cur_node = q.front();q.pop();
                if(cur_node->left != nullptr) q.push(cur_node->left);
                if(cur_node->right != nullptr) q.push(cur_node->right);
            }
        }
        findCommon(root, level, 0);
        return sol;
    }
};