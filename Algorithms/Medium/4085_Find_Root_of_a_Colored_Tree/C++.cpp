class Solution {
public:
    int findColoredRoot(vector<vector<int>>& edges, string colors) {
        int n = colors.size();
        unordered_map<char, char> nxt = {{'R', 'B'}, {'B', 'W'}, {'W', 'R'}};
        vector<int> in_degree(n), degree(n);
        for (auto edge : edges) {
            ++degree[edge[0]];
            ++degree[edge[1]];
            if (nxt[colors[edge[0]]] == colors[edge[1]])
                ++in_degree[edge[1]];
            else if (nxt[colors[edge[1]]] == colors[edge[0]])
                ++in_degree[edge[0]];
            else
                return -1;
        }

        int result = -1;
        for (int i = 0; i < n; ++i) {
            if (in_degree[i] > 1)
                return -1;

            if (in_degree[i] == 0)
                result = i;
        }
        
        return degree[result] <= 2 ? result : -1;
    }
};
