class Solution {
public:
    int maxArea(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        vector<vector<int>> dp(m, vector<int>(n));
        vector<int> row_max(m), col_max(n);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] == 1) {
                    if (i == 0 || j == 0)
                        dp[i][j] = 1;
                    else
                        dp[i][j] = 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});
                }
                
                row_max[i] = max(row_max[i], dp[i][j]);
                col_max[j] = max(col_max[j], dp[i][j]);
            }
        }
        
        vector<int> row_suffix(m+1), col_suffix(n+1);
        for (int i = m-1; i >= 0; --i)
            row_suffix[i] = max(row_suffix[i+1], row_max[i]);

        for (int j = n-1; j >= 0; --j)
            col_suffix[j] = max(col_suffix[j+1], col_max[j]);

        int result = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (dp[i][j] <= result)
                    continue;

                if (i+dp[i][j] < m && row_suffix[i+dp[i][j]] >= dp[i][j]) {
                    result = dp[i][j];
                    continue;
                }

                if (j+dp[i][j] < n && col_suffix[j+dp[i][j]] >= dp[i][j])
                    result = dp[i][j];
            }
        }
                
        return result * result;
    }
};
