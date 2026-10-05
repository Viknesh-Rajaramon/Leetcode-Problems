class Solution {
public:
    int longestSubarray(vector<int>& nums, int k) {
        int result = 0, n = nums.size();
        for (int l = 0; l < n; ++l) {
            long long curr_sum = 0;
            unordered_set<int> seen;
            for (int r = l; r < n; ++r) {
                curr_sum += nums[r];
                seen.insert(((2*nums[r] % k) + k) % k);
                int target = ((curr_sum % k) + k) % k;
                if (target == 0 || seen.count(target))
                    result = max(result, r-l+1);
            }
        }

        return result;
    }
};
