class Solution {
public:
    vector<long long> minTimeMaxPower(int n, vector<vector<int>>& edges, int power, vector<int>& cost, int source, int target) {
        vector<vector<pair<int, int>>> graph(n);
        for (auto edge : edges)
            graph[edge[0]].push_back({edge[1], edge[2]});
        
        vector<long long> cost_sp(n, LLONG_MAX), time(n, LLONG_MAX);
        priority_queue<tuple<long long, long long, int>, vector<tuple<long long, long long, int>>, greater<tuple<long long, long long, int>>> heap;
        heap.push({0, 0, source});
        cost_sp[source] = 0;
        time[source] = 0;
        while (!heap.empty()) {
            auto [t, d, u] = heap.top();
            heap.pop();

            if (d > power)
                continue;
            
            if (u == target)
                return {t, power-d};

            if (d + cost[u] > power)
                continue;
            
            for (auto& [v, w] : graph[u]) {
                if (d + cost[u] < cost_sp[v] || t + w < time[v]) {
                    cost_sp[v] = d + cost[u];
                    time[v] = t + w;
                    heap.push({t + w, d + cost[u], v});
                }
            }
        }
        
        return {-1, -1};
    }
};
