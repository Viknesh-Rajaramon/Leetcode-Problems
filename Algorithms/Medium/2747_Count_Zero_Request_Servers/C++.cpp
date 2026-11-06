class Solution {
public:
    vector<int> countServers(int n, vector<vector<int>>& logs, int x, vector<int>& queries) {
        sort(logs.begin(), logs.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });

        vector<int> ids(queries.size());
        iota(ids.begin(), ids.end(), 0);

        sort(ids.begin(), ids.end(), [&](int i, int j) {
            return queries[i] < queries[j];
        });

        vector<int> result(queries.size()), count(n+1);
        int l = 0, r = 0, active = 0;
        for (int i : ids) {
            while (r < logs.size() && logs[r][1] <= queries[i]) {
                int server = logs[r][0];
                if (count[server] == 0)
                    ++active;

                ++count[server];
                ++r;
            }

            int temp = queries[i] - x;
            while (l < r && logs[l][1] < temp) {
                int server = logs[l][0];
                --count[server];
                if (count[server] == 0)
                    --active;
                
                ++l;
            }

            result[i] = n - active;
        }

        return result;
    }
};
