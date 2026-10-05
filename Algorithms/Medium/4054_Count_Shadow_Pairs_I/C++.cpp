class Solution {
public:
    long long shadowPairs(vector<int>& nums) {
        long long result = 0, total = 0;
        vector<vector<int>> stack;
        for (int num : nums) {
            while (!stack.empty() && num < stack.back()[0]) {
                total -= stack.back()[1];
                stack.pop_back();
            }
            
            if (!stack.empty()) {
                result += total;
                if (stack.back()[0] == num) {
                    result -= stack.back()[1];
                    ++stack.back()[1];
                } else {
                    stack.push_back({num, 1});
                }
            } else {
                stack.push_back({num, 1});
            }
            
            ++total;
        }
        
        return result;
    }
};
