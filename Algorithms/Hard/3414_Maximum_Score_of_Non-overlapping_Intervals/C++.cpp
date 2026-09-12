class Solution {
public:
    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<int> arr(n), starts(n);
        for (int i = 0; i < n; ++i)
            arr[i] = i;
        
        sort(arr.begin(), arr.end(), [&](int a, int b) {
            return intervals[a][0] < intervals[b][0];
        });
        
        for (int i = 0; i < n; ++i) {
            starts[i] = intervals[arr[i]][0];
        }
        
        typedef pair<long long, vector<int>> State;
        State empty = {0, {}};
        vector<vector<State>> dp(n+1, vector<State>(5, empty));
        for (int i = n - 1; i >= 0; --i) {
            auto& row = dp[i];
            int idx = arr[i];
            auto it = upper_bound(starts.begin(), starts.end(), intervals[idx][1]);
            int nxt = distance(starts.begin(), it);
            for (int j = 1; j < 5; ++j) {
                State best = dp[i + 1][j];
                State sub = dp[nxt][j - 1];
                long long sc = sub.first + intervals[idx][2];
                if (sc > best.first) {
                    vector<int> cl = sub.second;
                    cl.push_back(idx);
                    sort(cl.begin(), cl.end());
                    best = {sc, cl};
                } else if (sc == best.first) {
                    vector<int> cl = sub.second;
                    cl.push_back(idx);
                    sort(cl.begin(), cl.end());
                    if (cl < best.second) {
                        best = {sc, cl};
                    }
                }
                row[j] = best;
            }
        }
        
        return dp[0][4].second;
    }
};
