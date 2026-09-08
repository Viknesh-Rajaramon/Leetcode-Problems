class Solution {
public:
    int shortestPath(int n, vector<vector<int>>& edges, string labels, int k) {
        vector<vector<pair<int, int>>> graph(n);
        for (auto edge : edges)
            graph[edge[0]].push_back({edge[1], edge[2]});
        
        vector<int> best_streak(n, k+1);
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> heap;
        heap.push({0, 1, 0});
        while (!heap.empty()) {
            auto [d, streak, u] = heap.top();
            heap.pop();
            if (streak >= best_streak[u])
                continue;

            best_streak[u] = streak;
            if (u == n-1)
                return d;

            for (auto& [v, w] : graph[u]) {
                int next_streak = labels[u] == labels[v] ? streak + 1 : 1;
                if (next_streak > k || next_streak >= best_streak[v])
                    continue;

                heap.push({d+w, next_streak, v});
            }
        }

        return -1;
    }
};
