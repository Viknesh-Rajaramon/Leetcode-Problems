class Solution {
public:
    long long elevatorRequests(int n, int start, vector<vector<int>>& requests) {
        sort(requests.begin(), requests.end(), [](const auto& a, const auto& b) {
            return a[1] < b[1];
        });
        n = requests.size();
        
        function<long long(long long, int, int)> min_time = [&](long long t_i, int i, int j) {
            long long t_j = t_i + abs(requests[j][1]-requests[i][1]);
            if (abs(j-i) == 1)
                return t_j;

            int k = j > i ? i+1 : i-1;
            long long t_k = t_i + abs(requests[k][1]-requests[i][1]);
            if (t_k >= requests[k][0])
                return min_time(t_k, k, j);

            if (t_j + abs(requests[k][1]-requests[j][1]) < requests[k][0])
                t_j = requests[k][0] - abs(requests[k][1]-requests[j][1]);

            return min(min_time(requests[k][0], k, j), min_time(t_j, j, k));
        };
        
        if (n == 1)
            return max(abs(start-requests[0][1]), requests[0][0]);

        long long t0 = max({requests[0][0], abs(requests[0][1]-start), requests[n-1][0]-abs(requests[n-1][1]-requests[0][1])});
        long long t1 = max({requests[n-1][0], abs(requests[n-1][1]-start), requests[0][0]-abs(requests[0][1]-requests[n-1][1])});

        return min(min_time(t0, 0, n-1), min_time(t1, n-1, 0));
    }
};
