class Solution {
public:
    int minCost(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        if (m == 1 && n == 1)
            return grid[0][0];
        
        vector<vector<int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        priority_queue<tuple<int, int, int, int, int>, vector<tuple<int, int, int, int, int>>, greater<tuple<int, int, int, int, int>>> heap;
        heap.push({grid[0][0], 0, 0, -1, 0});
        ++k;
        vector<vector<int>> dist(m, vector<int>(n, INT_MAX));
        vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(4, INT_MAX)));
        dist[0][0] = 0;
        while (!heap.empty()) {
            auto [val, r, c, prev_dir, moves] = heap.top();
            heap.pop();
            if (r == m-1 && c == n-1 && moves <= k)
                return val;

            if (prev_dir != -1) {
                if (moves >= dp[r][c][prev_dir])
                    continue;
                
                dp[r][c][prev_dir] = moves;
            }

            for (int d = 0; d < 4; ++d) {
                int nr = r + dirs[d][0], nc = c + dirs[d][1], new_moves = moves + (d != prev_dir ? 1 : 0);
                if (nr < 0 || nc < 0 || nr >= m || nc >= n || dist[nr][nc] < new_moves || new_moves > k)
                    continue;
                
                dist[nr][nc] = new_moves;
                heap.push({val + grid[nr][nc], nr, nc, d, new_moves});
            }
        }
        
        return -1;
    }
};
