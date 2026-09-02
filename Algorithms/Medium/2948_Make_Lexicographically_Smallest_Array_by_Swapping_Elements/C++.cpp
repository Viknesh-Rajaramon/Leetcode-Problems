class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        vector<int> ordered_nums(nums), group_start = {0};
        sort(ordered_nums.begin(), ordered_nums.end());
        unordered_map<int, int> num_to_group;
        int current_group = 0, prev = ordered_nums[0];
        for (int i = 0; i < ordered_nums.size(); ++i) {
            if (ordered_nums[i]-prev > limit) {
                ++current_group;
                group_start.push_back(i);
            }

            num_to_group[ordered_nums[i]] = current_group;
            prev = ordered_nums[i];
        }
        
        vector<int> result;
        for (int x : nums) {
            int group = num_to_group[x];
            result.push_back(ordered_nums[group_start[group]]);
            ++group_start[group];
        }

        return result;
    }
};
