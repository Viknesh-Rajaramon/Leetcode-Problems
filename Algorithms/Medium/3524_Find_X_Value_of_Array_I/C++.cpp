class Solution {
public:
    vector<long long> resultArray(vector<int>& nums, int k) {
        vector<long long> result(k), dp(k);
        for (int num : nums) {
            vector<long long> new_dp(k);
            ++new_dp[num % k];
            for (int r = 0; r < k; ++r)
                new_dp[(r * (num % k)) % k] += dp[r];

            dp = new_dp;
            for (int r = 0; r < k; ++r)
                result[r] += dp[r];
        }
        
        return result;
    }
};
