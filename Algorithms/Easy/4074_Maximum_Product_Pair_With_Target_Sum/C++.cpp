class Solution {
public:
    vector<int> maxProductPair(vector<int>& nums, int target) {
        vector<int> result = {-1, -1};
        int n = nums.size(), best = INT_MIN;
        unordered_map<int, int> index;
        for (int i = 0; i < n; ++i) {
            if (index.count(target - nums[i])) {
                int j = index[target - nums[i]];
                if (nums[i] != nums[j] && nums[i] * nums[j] > best) {
                    best = nums[i] * nums[j];
                    result = (nums[i] > nums[j]) ? vector<int>{i, j} : vector<int>{j, i};
                }
            }
            
            index[nums[i]] = i;
        }
        
        return result;
    }
};
