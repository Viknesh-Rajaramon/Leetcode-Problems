class Solution {
public:
    int minInversions(vector<string>& words, vector<int>& target) {
        int n = words.size();
        vector<int> pos(n);
        for (int p = 0; p < target.size(); ++p)
            pos[target[p]] = p;

        vector<unordered_map<char, int>> trie = {{}};
        vector<int> mark = {-1};
        for (int i = 0; i < n; ++i) {
            int u = 0;
            for (char c : words[i]) {
                if (!trie[u].count(c)) {
                    trie[u][c] = trie.size();
                    trie.push_back({});
                    mark.push_back(-1);
                }

                u = trie[u][c];
            }

            mark[u] = i;
        }
        
        function<int(vector<int>&, vector<int>&)> cross = [&](vector<int>& A, vector<int>& B) {
            int count = 0, j = 0;
            for (int x : A) {
                while (j < B.size() && B[j] < x)
                    ++j;
                
                count += j;
            }

            return count;
        };

        function<tuple<vector<int>, int>(int)> dfs = [&](int u) {
            int total = 0;
            vector<vector<int>> lists;
            for (auto& [_, v] : trie[u]) {
                auto [L, inv] = dfs(v);
                total += inv;
                lists.push_back(L);
            }

            int c = lists.size();
            if (c >= 2) {
                vector<vector<int>> cost(c, vector<int>(c));
                for (int a = 0; a < c; ++a) {
                    for (int b = a+1; b < c; ++b) {
                        int x = cross(lists[a], lists[b]);
                        cost[a][b] = x;
                        cost[b][a] = lists[a].size() * lists[b].size() - x;
                    }
                }
                
                int full = 1 << c;
                vector<vector<int>> add;
                for (int j = 0; j < c; ++j) {
                    vector<int> arr(full);
                    for (int mask = 1; mask < full; ++mask) {
                        int low = mask & -mask;
                        arr[mask] = arr[mask ^ low] + cost[bit_width((unsigned int)low) - 1][j];
                    }

                    add.push_back(arr);
                }

                vector<int> dp(full, INT_MAX);
                dp[0] = 0;
                for (int mask = 0; mask < full; ++mask) {
                    if (dp[mask] == INT_MAX)
                        continue;
                    
                    for (int j = 0; j < c; ++j) {
                        int bit = 1 << j;
                        if (!(mask & bit)) {
                            int nd = dp[mask] + add[j][mask];
                            if (nd < dp[mask | bit])
                                dp[mask | bit] = nd;
                        }
                    }
                }
                
                total += dp[full - 1];
            }

            vector<int> merged;
            for (vector<int>& L : lists)
                merged.insert(merged.end(), L.begin(), L.end());

            sort(merged.begin(), merged.end());
            if (mark[u] >= 0) {
                total += lower_bound(merged.begin(), merged.end(), pos[mark[u]]) - merged.begin();
                merged.push_back(pos[mark[u]]);
                sort(merged.begin(), merged.end());
            }

            return tuple{merged, total};
        };

        return get<1>(dfs(0));
    }
};
