class Solution {
public:
    int countSpecialIntegers(vector<int>& nums) {
        unordered_map<int, vector<int>> pos;
        for (int i = 0; i < nums.size(); ++i)
            pos[nums[i]].push_back(i);
        
        int result = 0;
        for (auto& [_, indices] : pos) {
            if (indices.size() < 3)
                continue;
            
            bool special = true;
            int diff = indices[1] - indices[0];
            for (int i = 1; i < indices.size()-1; ++i) {
                if (indices[i+1] - indices[i] != diff) {
                    special = false;
                    break;
                }
            }
            
            if (special)
                ++result;
        }

        return result;
    }
};
