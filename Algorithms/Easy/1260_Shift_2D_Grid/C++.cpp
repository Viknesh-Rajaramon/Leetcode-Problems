class Solution {
public:
    void shift(vector<vector<int>>& grid, int i, int j, int n) {
        while (i < j) {
            swap(grid[i/n][i%n], grid[j/n][j%n]);
            ++i;
            --j;
        }
    }

    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        int total = m*n;
        k %= total;

        shift(grid, 0, total-1, n);
        shift(grid, 0, k-1, n);
        shift(grid, k, total-1, n);

        return grid;
    }
};
