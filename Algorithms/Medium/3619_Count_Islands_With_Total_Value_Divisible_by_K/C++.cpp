class Solution {
public:
    int countIslands(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        vector<tuple<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        function<long long(int, int)> dfs = [&](int i, int j) {
            if (grid[i][j] == 0)
                return 0LL;
            
            long long sum_ = grid[i][j];
            grid[i][j] = 0;
            for (auto [dx, dy] : directions) {
                int x = i+dx, y = j+dy;
                if (x < 0 || x >= m || y < 0 || y >= n || grid[x][y] == 0)
                    continue;

                sum_ += dfs(x, y);
            }

            return sum_;
        };
        
        int result = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 0)
                    continue;
                
                if (dfs(i, j)%k == 0)
                    ++result;
            }
        }
        
        return result;
    }
};
