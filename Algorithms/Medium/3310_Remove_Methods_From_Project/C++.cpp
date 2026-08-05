class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& invocations) {
        vector<vector<int>> edges(n);
        for (const auto& inv: invocations)
            edges[inv[0]].push_back(inv[1]);
        
        vector<bool> suspicious(n, false);
        suspicious[k] = true;
        
        queue<int> q;
        q.push(k);
        while (!q.empty()) {
            int u = q.front();
            q.pop();

            for (int v: edges[u]) {
                if (!suspicious[v]) {
                    suspicious[v] = true;
                    q.push(v);
                }
            }
        }

        for (const auto& inv: invocations) {
            if (!suspicious[inv[0]] && suspicious[inv[1]]) {
                vector<int> result(n);
                for (int i = 0; i < n; ++i)
                    result[i] = i;
                
                return result;
            }
        }
        
        vector<int> result;
        for (int i = 0; i < n; ++i)
            if (!suspicious[i])
                result.push_back(i);

        return result;
    }
};
