class Solution {
public:
    int minOperations(vector<int>& nums, int sum) {
        int Max = 1e9+7;
        vector<int> dp(sum+1, Max);
        dp[0] = 0;
        for (int num : nums) {
            vector<int> new_dp(dp.begin(), dp.end());
            int n = num, count = 0;
            while (n > 0) {
                for (int i = sum; i >= n; --i)
                    new_dp[i] = min(new_dp[i], dp[i-n] + count);
                    
                ++count;
                n >>= 1;
            }
            
            n = num << 1;
            count = 1;
            while (n <= sum) {
                for (int i = sum; i >= n; --i)
                    new_dp[i] = min(new_dp[i], dp[i-n] + count);

                ++count;
                n <<= 1;
            }
                
            dp = new_dp;
        }

        return dp[sum] != Max ? dp[sum] : -1;
    }
};
