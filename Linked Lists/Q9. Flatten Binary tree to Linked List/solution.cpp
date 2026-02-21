class Solution {
public:
    TreeNode* prev = NULL;

    void flatten(TreeNode* root) {
        if (root == NULL) return;

        // First flatten right subtree
        flatten(root->right);

        // Then flatten left subtree
        flatten(root->left);

        // Rewire pointers
        root->right = prev;
        root->left = NULL;

        // Move prev to current node
        prev = root;
    }
};
