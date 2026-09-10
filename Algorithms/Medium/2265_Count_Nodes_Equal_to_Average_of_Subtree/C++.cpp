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
    int result;
    
    tuple<int, int> dfs(TreeNode* node) {
        if (node == nullptr)
            return {0, 0};
        
        int left_sum, left_nodes, right_sum, right_nodes;
        tie(left_sum, left_nodes) = dfs(node->left);
		tie(right_sum, right_nodes) = dfs(node->right);

        int sum_ = left_sum + right_sum + node->val, nodes_ = left_nodes + right_nodes + 1;
        if (sum_/nodes_ == node->val)
            ++result;
        
        return {sum_, nodes_};
    }

    int averageOfSubtree(TreeNode* root) {
        dfs(root);
        return result;
    }
};
