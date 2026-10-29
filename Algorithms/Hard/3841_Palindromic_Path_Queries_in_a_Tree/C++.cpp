class FenwickTree {
private:
    int n;
    vector<int> tree;

public:
    FenwickTree(int n) : n(n), tree(n+1) {}

    void update(int i, int val) {
        while (i <= n) {
            tree[i] ^= val;
            i += i & -i;
        }
    }

    int query(int i) {
        int result = 0;
        while (i > 0) {
            result ^= tree[i];
            i -= i & -i;
        }

        return result;
    }

    void update_range(int l, int r, int val) {
        update(l, val);
        update(r+1, val);
    }
};

class Solution {
public:
    vector<bool> palindromePath(int n, vector<vector<int>>& edges, string s, vector<string>& queries) {
        vector<vector<int>> graph(n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        int LOG = 32 - __builtin_clz(n), timer = 0;
        vector<vector<int>> parent(n, vector<int> (LOG));
        vector<int> depth(n), tin(n), tout(n);
        function<void(int, int)> dfs = [&](int u, int par) {
            tin[u] = ++timer;
            parent[u][0] = par;
            for (int v : graph[u]) {
                if (v == par)
                    continue;
                
                depth[v] = depth[u]+1;
                dfs(v, u);
            }
        
            tout[u] = timer;
        };

        dfs(0, 0);
        for (int j = 1; j < LOG; ++j) {
            for (int i = 0; i < n; ++i)
                parent[i][j] = parent[parent[i][j-1]][j-1];
        }

        function<int(int, int)> lca = [&](int u, int v) {
            if (depth[u] < depth[v])
                swap(u, v);
            
            int diff = depth[u] - depth[v];
            for (int i = 0; i < LOG; ++i)
                if ((diff & (1 << i)) != 0)
                    u = parent[u][i];
            
            if (u == v)
                return u;
            
            for (int i = LOG-1; i >= 0; --i) {
                if (parent[u][i] != parent[v][i]) {
                    u = parent[u][i];
                    v = parent[v][i];
                }
            }
            
            return parent[u][0];
        };

        FenwickTree ft(n+1);
        for (int u = 0; u < n; ++u)
            ft.update_range(tin[u], tout[u], 1 << (s[u] - 'a'));
        
        vector<bool> result;
        for (string& q : queries) {
            stringstream ss(q);
            string op;
            ss >> op;
            if (op == "update") {
                int u;
                char c;
                ss >> u >> c;
                ft.update_range(tin[u], tout[u], (1 << (s[u]-'a')) ^ (1 << (c-'a')));
                s[u] = c;
            } else {
                int u, v;
                ss >> u >> v;
                int path_mask = ft.query(tin[u]) ^ ft.query(tin[v]) ^ (1 << (s[lca(u, v)]-'a'));
                result.push_back((path_mask & (path_mask-1)) == 0);
            }
        }

        return result;
    }
};
