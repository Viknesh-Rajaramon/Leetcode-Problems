class Solution {
public:
    int subsequencePairCount(vector<int>& nums) {
        int mod = 1000000007, m = *max_element(nums.begin(), nums.end());
        vector<vector<int>> dp(m+1, vector<int>(m+1));
        dp[0][0] = 1;
        for (int num: nums) {
            vector<vector<int>> new_dp(m+1, vector<int>(m+1));
            for (int i = 0; i <= m; ++i) {
                int div_1 = gcd(i, num);
                for (int j = 0; j <= m; ++j) {
                    if (dp[i][j] == 0)
                        continue;

                    int div_2 = gcd(j, num);
                    new_dp[i][j] = (new_dp[i][j] + dp[i][j]) % mod;
                    new_dp[div_1][j] = (new_dp[div_1][j] + dp[i][j]) % mod;
                    new_dp[i][div_2] = (new_dp[i][div_2] + dp[i][j]) % mod;
                }
            }

            dp.swap(new_dp);
        }

        int result = 0;
        for (int i = 1; i <= m; ++i)
            result = (result + dp[i][i]) % mod;

        return result;
    }
};
