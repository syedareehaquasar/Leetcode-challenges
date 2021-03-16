/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rob(TreeNode* root) {
        if (!root) return 0;
        int ans = 0;
        if (root -> right) ans += rob(root -> right -> right) + rob(root -> right -> left);
        if (root -> left) ans += rob(root -> left -> right) + rob(root -> left -> left);
        return max(ans + root -> val, rob(root -> left) + rob(root -> right));
    }
};
