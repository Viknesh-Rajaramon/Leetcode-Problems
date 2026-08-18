class Solution {
public:
    int largestInteger(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int, int> hash_map;
        for (int i = 0; i <= n-k; ++i) {
            set<int> s(nums.begin()+i, nums.begin()+i+k);
            for (int num : s)
                ++hash_map[num];
        }

        int result = -1;
        for (auto it : hash_map)
            if (it.second == 1)
                result = max(result, it.first);

        return result;
    }
};
