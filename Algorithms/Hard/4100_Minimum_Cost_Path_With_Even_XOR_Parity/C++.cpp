class Solution {
public:
    int minActivationCost(vector<vector<int>>& edges, vector<int>& values) {
        int n = values.size();
        vector<vector<vector<int>>> graph(n);
        for (vector<int> &edge : edges) {
            int u = edge[0], v = edge[1], c = edge[2];
            graph[u].push_back({v, c});
            graph[v].push_back({u, c});
        }

        function<int(int, int)> add = [&](int a, int b) {
            if (a == INT_MAX || b == INT_MAX || a > INT_MAX-b)
                return INT_MAX;
            
            return a + b;
	    };
        
        int result = INT_MAX;
        function<vector<int>(int, int)> dfs = [&](int u, int parent) {
            int b = __builtin_popcount(values[u]) & 1;
            vector<int> f = {INT_MAX, INT_MAX};
            f[b] = 0;
            for (vector<int>& edge : graph[u]) {
                int v = edge[0], c = edge[1];
                if (v == parent)
                    continue;

                vector<int> g = dfs(v, u);
                result = min(result, add(min(add(f[0], g[0]), add(f[1], g[1])), c));
                f[b] = min(f[b], add(g[0], c));
                f[b^1] = min(f[b^1], add(g[1], c));
            }

            return f;
        };

        dfs(0, -1);
        return result != INT_MAX ? result : -1;
    }
};
