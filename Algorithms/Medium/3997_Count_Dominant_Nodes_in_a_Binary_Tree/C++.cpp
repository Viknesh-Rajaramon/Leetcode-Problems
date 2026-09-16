/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int countDominantNodes(TreeNode* root) {
        int result = 0;
        function<int(TreeNode*)> postorder = [&](TreeNode* node) {
            if (node == nullptr)
                return 0;

            int left_max = postorder(node->left);
            int right_max = postorder(node->right);
            if (node->val >= left_max && node->val >= right_max) {
                ++result;
                return node->val;
            }

            return max(left_max, right_max);
        };

        postorder(root);
        return result;
    }
};
