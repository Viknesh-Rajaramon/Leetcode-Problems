class Solution {
public:
    long long elevatorRequests(int n, int start, vector<int>& requests) {
        bool found = false;
        for (int r : requests) {
            if (r == start) {
                found = true;
                break;
            }
        }

        if (!found)
            requests.push_back(start);

        sort(requests.begin(), requests.end());
        int m = requests.size();
        vector<vector<long long>> dp_0(m, vector<long long>(m, LLONG_MAX)), dp_1(m, vector<long long>(m, LLONG_MAX));
        start = distance(requests.begin(), lower_bound(requests.begin(), requests.end(), start));
        dp_0[start][start] = 0;
        dp_1[start][start] = 0;
        for (int l = 1; l < m; ++l) {
            long long rem = m-l;
            for (int i = 0; i <= m-l; ++i) {
                int j = i+l-1;
                if (dp_0[i][j] != LLONG_MAX) {
                    if (i > 0)
                        dp_0[i-1][j] = min(dp_0[i-1][j], dp_0[i][j] + rem*(requests[i]-requests[i-1]));

                    if (j < m-1)
                        dp_1[i][j+1] = min(dp_1[i][j+1], dp_0[i][j] + rem*(requests[j+1]-requests[i]));
                }

                if (dp_1[i][j] != LLONG_MAX) {
                    if (i > 0)
                        dp_0[i-1][j] = min(dp_0[i-1][j], dp_1[i][j] + rem*(requests[j]-requests[i-1]));

                    if (j < m-1)
                        dp_1[i][j+1] = min(dp_1[i][j+1], dp_1[i][j] + rem*(requests[j+1]-requests[j]));
                }
            }
        }

        return min(dp_0[0][m-1], dp_1[0][m-1]);
    }
};
