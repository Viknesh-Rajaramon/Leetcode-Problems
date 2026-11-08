class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        int result = 0, m = grid.size(), n = grid[0].size();
        for (int r = 0; r < m; ++r) {
            int count = 0, idx = -1;
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 1) {
                    if (count == 0)
                        idx = c;

                    ++count;
                }
            }

            bool can_comm = (count != 1);
            if (!can_comm) {
                for (int i = 0; i < m; ++i) {
                    if (i != r && grid[i][idx] == 1) {
                        can_comm = true;
                        break;
                    }
                }
            }
            
            if (can_comm)
                result += count;
        }

        return result;
    }
};
