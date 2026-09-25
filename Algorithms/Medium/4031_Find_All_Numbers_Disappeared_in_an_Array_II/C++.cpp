class Solution {
public:
    vector<vector<int>> findDisappearedNumbers(vector<int>& nums, int lower, int upper) {
        vector<vector<int>>result;
        set<int>nums_set(nums.begin(), nums.end());
        int start = lower;
        for (int end = lower; end <= upper; ++end) {
            if (nums_set.find(end) != nums_set.end()) {
                if (start != end)
                    result.push_back(vector<int>{start, end-1});
                
                start = end+1;
            } else if (end == upper)
                result.push_back(vector<int>{start, end});
        }

        return result;
    }
};
