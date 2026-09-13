class Solution {
public:
    int maxConsistentColumns(vector<vector<int>>& grid, int limit) {
        int m = grid.size(), n = grid[0].size();
        vector<int> dp(n, 1);

        for (int j = 1; j < n; ++j) {
            for (int k = 0; k < j; ++k) {
                bool is_valid = true;
                for (int i = 0; i < m; ++i) {
                    if (abs(grid[i][j] - grid[i][k]) > limit) {
                        is_valid = false;
                        break;
                    }
                }

                if (is_valid)
                    dp[j] = max(dp[j], dp[k]+1);
            }
        }

        int result = 1;
        for (int val : dp)
            result = max(result, val);

        return result;
    }
};
