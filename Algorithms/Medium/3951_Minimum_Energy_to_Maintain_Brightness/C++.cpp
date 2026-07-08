class Solution {
public:
    long long minEnergy(int n, int brightness, vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        long long time = 0, start = intervals[0][0], end = intervals[0][1];
        for (int i = 1; i < intervals.size(); ++i) {
            if (intervals[i][0] <= end) {
                end = max(end, (long long)intervals[i][1]);
            } else {
                time += end-start+1;
                start = intervals[i][0];
                end = intervals[i][1];
            }
        }

        time += end-start+1;
        return ((brightness+2)/3) * time;
    }
};
