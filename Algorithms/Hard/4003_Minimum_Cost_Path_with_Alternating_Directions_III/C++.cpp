class Solution {
public:
    long long minCost(int m, int n, vector<vector<int>>& penalty) {
        vector<tuple<int, int, int>> moves = {{0, 1, 0}, {1, 0, 0}, {0, -1, 1}, {-1, 0, 1}};
        vector<vector<vector<long long>>> dist(m, vector<vector<long long>>(n, vector<long long>(2, LLONG_MAX)));
        dist[0][0][0] = 1;
        priority_queue<tuple<long long, int, int, int>, vector<tuple<long long, int, int, int>>, greater<tuple<long long, int, int, int>>> pq;
        pq.push({1, 0, 0, 0});
        while (!pq.empty()){
            tuple<long long, int, int, int> state = pq.top();
            long long cost = get<0>(state);
            int i = get<1>(state), j = get<2>(state), parity = get<3>(state);
            pq.pop();

            if (cost != dist[i][j][parity])
                continue;
            
            if (i == m-1 && j == n-1)
                return cost;
            
            long long new_cost = cost + penalty[i][j];
            int new_parity = 1 ^ parity;
            if (new_cost < dist[i][j][new_parity]) {
                dist[i][j][new_parity] = new_cost;
                pq.push({new_cost, i, j, new_parity});
            }
            
            for (auto& [di, dj, allowed_parity] : moves) {
                int ni = i+di, nj = j+dj;
                if (ni < 0 || ni >= m || nj < 0 || nj >= n)
                    continue;
                
                long long move_cost = (ni+1)*(nj+1) + (parity == allowed_parity ? 0 : penalty[i][j]);
                long long new_cost = cost + move_cost;
                int new_parity = 1 ^ parity;
                if (new_cost < dist[ni][nj][new_parity]) {
                    dist[ni][nj][new_parity] = new_cost;
                    pq.push({new_cost, ni, nj, new_parity});
                }
            }
        }
        
        return -1;
    }
};
