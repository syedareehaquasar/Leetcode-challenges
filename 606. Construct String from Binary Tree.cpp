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
    string tree2str(TreeNode* t) {
        if (!t) return "";
        string ans = to_string(t -> val);
        string l = tree2str(t -> left); 
        string r = tree2str(t -> right); 
        if ( l.empty() && r.empty()) return ans;
        else if (l.empty()) ans = ans + "()" + "(" + r + ")";
        else if (r.empty()) ans = ans + "(" + l + ")";
        else ans = ans + "(" + l + ")" + "(" + r + ")";
        return ans;
    }
};
