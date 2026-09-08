class Solution {
public:
    long long dfs(int u, vector<vector<int>>& tree, vector<int>& baseTime) {
        if (tree[u].size() == 0)
            return baseTime[u];
        
        long long earliest = LLONG_MAX, latest = LLONG_MIN;
        for (int v : tree[u]) {
            long long finish = dfs(v, tree, baseTime);
            earliest = min(earliest, finish);
            latest = max(latest, finish);
        }

		return latest + (latest - earliest) + baseTime[u];
    }


    long long finishTime(int n, vector<vector<int>>& edges, vector<int>& baseTime) {
        vector<vector<int>> tree(n);
        for (int i = 0; i < edges.size(); ++i)
            tree[edges[i][0]].push_back(edges[i][1]);

	    return dfs(0, tree, baseTime);
    }
};
