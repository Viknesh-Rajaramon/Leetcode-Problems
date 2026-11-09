class Solution {
public:
    long long minCost(int n, string colors, vector<vector<int>>& edges) {
        vector<vector<int>> g(n);
        for (auto edge : edges) {
            g[edge[0]].push_back(edge[1]);
            g[edge[1]].push_back(edge[0]);
        }

        struct State {
            int size;
            long long cost_B;
            long long cost_R;
            long long cost_BR;
        };

        function<State(int, int)> dfs = [&](int u, int parent) {
            int size = 1;
            long long cost_B = 0, cost_R = 0;
            vector<long long> t;
            for (int v : g[u]) {
                if (v == parent)
                    continue;
                
                State curr = dfs(v, u);
                size += curr.size;
                cost_B += curr.cost_B;
                cost_R += min(curr.cost_R, curr.cost_B);
                t.push_back(curr.cost_B - min(curr.cost_R, curr.cost_BR));
            }

            sort(t.rbegin(), t.rend());
            cost_B += colors[u] == 'B' ? 0 : size;
            cost_R += colors[u] == 'R' ? 0 : size;

            long long cost_BR = t.size() > 0 ? cost_B - t[0] : 0;
            return State{size, cost_B, cost_R, cost_BR};
        };           
        
        State result = dfs(0, -1);
        return min({result.cost_B, result.cost_R, result.cost_BR});
    }
};
