class Solution {
public:
    int minMoves(vector<string>& classroom, int energy) {
        int m = classroom.size(), n = classroom[0].size(), k = 0, sr = 0, sc = 0;
        vector<vector<int>> dp(m, vector<int>(n, -1));
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (classroom[r][c] == 'S') {
                    sr = r;
                    sc = c;
                } else if (classroom[r][c] == 'L') {
                    dp[r][c] = k++;
                }
            }
        }

        if (k == 0)
            return 0;
        
        int total_mask = (1 << k)-1;
        vector<vector<vector<int>>> best(m, vector<vector<int>>(n, vector<int>(1<<k, -1)));

        struct State {
            int r, c, mask, energy, moves;
        };

        best[sr][sc][0] = energy;
        queue<State> q;
        int dr[] = {-1, 1, 0, 0}, dc[] = {0, 0, -1, 1};

        q.push({sr, sc, 0, energy, 0});
        while (!q.empty()) {
            State curr = q.front();
            q.pop();

            if (curr.energy == 0)
                continue;
            
            for (int d = 0; d < 4; ++d) {
                int nr = curr.r + dr[d], nc = curr.c + dc[d];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || classroom[nr][nc] == 'X')
                    continue;
                
                int ne = curr.energy-1, nmask = curr.mask;
                if (classroom[nr][nc] == 'R')
                    ne = energy;

                if (classroom[nr][nc] == 'L')
                    nmask |= 1 << dp[nr][nc];

                if (nmask == total_mask)
                    return curr.moves + 1;

                if (ne <= best[nr][nc][nmask])
                    continue;

                best[nr][nc][nmask] = ne;
                q.push({nr, nc, nmask, ne, curr.moves + 1});
            }
        }

        return -1;
    }
};
