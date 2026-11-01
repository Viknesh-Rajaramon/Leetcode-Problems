class Solution {
public:
    int minMergedInteger(vector<int>& nums) {
        int result = INT_MAX;
        for (int i = 0; i < nums.size(); i += 2)
            result = min(result, stoi(to_string(nums[i]) + to_string(nums[i+1])));

        return result;
    }
};
