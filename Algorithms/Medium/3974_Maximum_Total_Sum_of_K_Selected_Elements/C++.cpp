class Solution {
public:
    long long maxSum(vector<int>& nums, int k, int mul) {
        sort(nums.begin(), nums.end(), greater<int>());
        long long result = 0;
        int end = min(k, mul-1);
        for (int i = 0; i < end; ++i)
            result += (1LL * nums[i] * mul--);

        for (int i = end; i < k; ++i)
            result += nums[i];

        return result;
    }
};
