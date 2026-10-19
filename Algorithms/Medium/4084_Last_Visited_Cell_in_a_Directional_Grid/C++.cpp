class Solution {
public:
    vector<int> lastVisitedCell(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size(), r = 0, c = 0;
        while (true) {
            char move = grid[r][c];
            grid[r][c] = 'V';
            int nr = r, nc = c;
            if (move == 'R')
                ++nc;
            else if (move == 'L')
                --nc;
            else if (move == 'D')
                ++nr;
            else if (move == 'U')
                --nr;

            if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 'V')
                return {r, c};

            r = nr;
            c = nc;
        }
            

        return {r, c};
    }
};
