class Solution {
public:
    bool canRemoveAll(vector<int>& types, vector<int>& colors, vector<int>& groupSize) {
        vector<vector<int>> stack;
        for (int i = 0; i < types.size(); ++i) {
            if (!stack.empty() && stack.back()[0] == types[i] && stack.back()[1] == colors[i])
                ++stack.back()[2];
            else
                stack.push_back({types[i], colors[i], 1});
            
            if (stack.back()[2] == groupSize[types[i]])
                stack.pop_back();
        }
        
        return stack.empty();
    }
};
