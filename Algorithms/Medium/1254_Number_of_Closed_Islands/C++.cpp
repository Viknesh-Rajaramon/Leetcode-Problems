class Solution {
public:
    int closedIsland(vector<vector<int>>& grid) {
        int result = 0, m = grid.size(), n = grid[0].size();
        function<bool(int, int)> dfs = [&](int r, int c) {
            if (r < 0 || r >= m || c < 0 || c >= n)
                return false;
            
            if (grid[r][c] == 1)
                return true;
            
            grid[r][c] = 1;
            bool left = dfs(r, c-1), right = dfs(r, c+1), up = dfs(r-1, c), down = dfs(r+1, c);
            return left && right && up && down;
        };

        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 0 && dfs(r, c))
                    ++result;
            }
        }

        return result;
    }
};
