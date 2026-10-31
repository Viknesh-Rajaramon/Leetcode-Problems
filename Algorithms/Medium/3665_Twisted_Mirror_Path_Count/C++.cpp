class Solution {
public:
    int uniquePaths(vector<vector<int>>& grid) {
        int n = grid[0].size(), mod = 1e9+7;
        vector<int> dp(n);
        dp[0] = 1;
        for (vector<int>& row : grid) {
            vector<int> prev_dp(dp.begin(), dp.end());
            dp.assign(n, 0);
            int prev = 0;
            for (int i = 0; i <n; ++i) {
                if (row[i] == 0) {
                    dp[i] = (prev + prev_dp[i]) % mod;
                    prev = (prev + prev_dp[i]) % mod;
                } else {
                    dp[i] = prev;
                    prev = prev_dp[i];
                }
            }
        }
        
        return dp[n-1];
    }
};
