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
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        unordered_map<int, TreeNode*> nodes;
        for (int i = 0; i < descriptions.size(); ++i)
            if (nodes[descriptions[i][1]] == 0)
                nodes[descriptions[i][1]] = new TreeNode(descriptions[i][1]);

        TreeNode* root;
        for (int i = 0; i < descriptions.size(); ++i) {
            if (nodes[descriptions[i][0]] == 0) {
                root = new TreeNode(descriptions[i][0]);
                nodes[descriptions[i][0]] = root;
            }

            if (descriptions[i][2] == 1)
                nodes[descriptions[i][0]]->left = nodes[descriptions[i][1]];
            else
                nodes[descriptions[i][0]]->right = nodes[descriptions[i][1]];
        }

        return root;
    }
};
