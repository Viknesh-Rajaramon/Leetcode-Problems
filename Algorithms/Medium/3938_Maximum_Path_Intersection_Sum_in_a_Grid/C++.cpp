class Solution {
public:
    int maxScore(vector<vector<int>>& grid) {
        int result = INT_MIN, m = grid.size(), n = grid[0].size();
        for (int i = 1; i < m-1; ++i)
            for (int j = 1; j < n-1; j++)
                result = max(result, grid[i][j]);

        for (int i = 0; i < m; ++i) {
            int curr_sum = grid[i][0];
            for (int j = 1; j < n; ++j) {
                curr_sum = max(curr_sum, grid[i][j-1]) + grid[i][j];
                result = max(result, curr_sum);
            }
        }

        for (int j = 0; j < n; ++j) {
            int curr_sum = grid[0][j];
            for (int i = 1; i < m; ++i) {
                curr_sum = max(curr_sum, grid[i-1][j]) + grid[i][j];
                result = max(result, curr_sum);
            }
        }
        
        return result;
    }
};
