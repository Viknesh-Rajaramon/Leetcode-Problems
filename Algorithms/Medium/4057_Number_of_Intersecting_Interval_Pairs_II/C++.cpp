class Solution {
public:
    long long countIntersectingIntervals(vector<vector<int>>& intervals) {
        long long result = 0;
        int n = intervals.size(), i = 0;
        vector<int> starts(n), ends(n);
        for (int j = 0; j < n; ++j) {
            starts[j] = intervals[j][0];
            ends[j] = intervals[j][1];
        }

        sort(starts.begin(), starts.end());
        sort(ends.begin(), ends.end());

        for (int j = 0; j < n; ++j) {
            while (i < n && ends[i] < starts[j])
                ++i;

            result += j-i;
        }

        return result;
    }
};
