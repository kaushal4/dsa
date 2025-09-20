class Solution {
public:
    TreeNode* itr(TreeNode* root, int left, int right){
        if(root == nullptr) return nullptr;
        if(root->val < left && root->val < right){
            return itr(root->right, left, right);
        } 
        if(root->val > left && root->val > right){
            return itr(root->left, left, right);
        } 
        return root;
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        int left = p->val;
        int right = q->val;
        return itr(root, left, right);
    }
};