class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<unordered_set<int>> dp(n);
        dp[0].insert(grid[0][0]);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 && j == 0)
                    continue;
                
                unordered_set<int> curr;
                if (i > 0) {
                    for (int val : dp[j])
                        curr.insert(val ^ grid[i][j]);
                }

                if (j > 0) {
                    for (int val : dp[j-1])
                        curr.insert(val ^ grid[i][j]);
                }

                dp[j] = curr;
            }
        }
        
        return *min_element(dp[n-1].begin(), dp[n-1].end());
    }
};
