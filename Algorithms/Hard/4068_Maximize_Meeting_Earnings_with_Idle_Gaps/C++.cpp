class Solution {
public:
    long long maxEarnings(vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[1] < b[1]; 
        });

        long long result = 0;
        vector<long long> ends = {-1}, best = {LLONG_MIN};
        for (auto& meeting : meetings) {
            long long start = meeting[0], end = meeting[1], revenue = meeting[2];
            int pos = upper_bound(ends.begin(), ends.end(), start) - ends.begin();
            long long prev = start + best[pos-1];
            if (prev > 0)
                revenue += prev;

            result = max(result, revenue);
            if (revenue-end > best.back()) {
                ends.push_back(end);
                best.push_back(revenue-end);
            }
        }

        return result;
    }
};
