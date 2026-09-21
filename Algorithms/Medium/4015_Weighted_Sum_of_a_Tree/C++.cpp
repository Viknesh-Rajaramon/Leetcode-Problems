class Solution {
public:
    long long weightedSum(vector<int>& parent, vector<int>& nums) {
        int n = parent.size();
        vector<vector<int>> tree(n);
        vector<int> depth(n, -1);
        for (int i = 1; i < n; ++i)
            tree[parent[i]].push_back(i);
        
        function<void(int, int)> dfs = [&](int u, int d) {
            depth[u] = d;
            for (int v : tree[u])
                dfs(v, d+1);
        };
        
        dfs(0, 0);

        int height = 0;
        for (int d : depth)
            height = max(height, d);
        ++height;
        
        long long result = 0;
        for (int i = 0; i < n; ++i)
            result += 1LL * nums[i] * (height - depth[i]);
        
        return result;
    }
};
