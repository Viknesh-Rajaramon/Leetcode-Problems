class Solution {
public:
    bool hasValidPath(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        if ((m+n-1)%2 == 1)
            return false;
        
        if (grid[0][0] != '(' || grid[m-1][n-1] != ')')
            return false;
        
        set<tuple<int, int, int>> visited;
        function<bool(int, int, int)> dfs = [&](int i, int j, int k) {
            k += (grid[i][j] == '(' ? 1 : -1);
            if (k < 0 || k > m-i+n-j-1)
                return false;
            
            if (i == m-1 && j == n-1)
                return k == 0;
            
            tuple<int, int, int> state = {i, j, k};
            if (visited.count(state))
                return false;
            
            visited.insert(state);
            if (i+1 < m && dfs(i+1, j, k))
                return true;
            
            if (j+1 < n && dfs(i, j+1, k))
                return true;
            
            return false;
        };

        return dfs(0, 0, 0);
    }
};
