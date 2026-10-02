class Solution {
public:
    int countSpecialIntegers(vector<int>& nums) {
        unordered_map<int, vector<int>> pos;
        for (int i = 0; i < nums.size(); ++i)
            pos[nums[i]].push_back(i);
        
        int result = 0;
        for (auto& [_, indices] : pos)
            if (indices.size() == 3 && 2*indices[1] == indices[0] + indices[2])
                ++result;

        return result;
    }
};
