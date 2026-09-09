class Solution {
public:
    int maxValidPairSum(vector<int>& nums, int k) {
        int result = INT_MIN, left_max = INT_MIN;
        for (int r = k; r < nums.size(); ++r) {
            left_max = max(left_max, nums[r-k]);
            result = max(result, left_max + nums[r]);
        }

        return result;
    }
};
