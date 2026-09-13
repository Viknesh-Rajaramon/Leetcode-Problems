class Solution {
public:
    vector<string> createGrid(int m, int n, int k) {
        vector<vector<string>> grid(m, vector<string>(n, "#"));
        vector<vector<int>> dp(m, vector<int>(n));
        int r = min(m, 4), c = min(n, 4);

        function<bool(int, int)> backtrack = [&](int i, int j) {
            if (i == r)
                return dp[r-1][c-1] == k;
            
            int next_i = i, next_j = j+1;
            if (next_j == c) {
                next_i = i+1;
                next_j = 0;
            }

            grid[i][j] = ".";
            if (i == 0 && j == 0)
                dp[i][j] = 1;
            else
                dp[i][j] = (i > 0 ? dp[i-1][j] : 0) + (j > 0 ? dp[i][j-1] : 0);
            
            if (backtrack(next_i, next_j))
                return true;
            
            grid[i][j] = "#";
            dp[i][j] = 0;
            if (!((i == 0 && j == 0) || (i == r-1 && j == c-1))) {
                if (backtrack(next_i, next_j))
                    return true;
            }

            return false;
        };

        if (!backtrack(0, 0))
            return vector<string>{};
        
        for (int j = c-1; j < n; ++j)
            grid[r-1][j] = ".";

        for (int i = r-1; i < m; ++i)
            grid[i][n-1] = ".";

        vector<string> result(m);
        for (int i = 0; i < m; ++i)
            result[i] = accumulate(grid[i].begin(), grid[i].end(), string(""));

        return result;
    }
};
