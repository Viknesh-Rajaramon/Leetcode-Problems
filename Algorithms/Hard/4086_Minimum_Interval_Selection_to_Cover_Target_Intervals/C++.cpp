class Solution {
public:
    int minSelection(vector<vector<int>>& availableIntervals, vector<vector<int>>& targetIntervals) {
        sort(targetIntervals.begin(), targetIntervals.end());
        sort(availableIntervals.begin(), availableIntervals.end());
        int result = 0, n = availableIntervals.size(), i = 0, curr = 0, best = 0;
        for (auto target : targetIntervals) {
            int s = target[0], e = target[1];
            while (curr < e) {
                int t = max(curr, s);
                while (i < n && availableIntervals[i][0] <= t) {
                    best = max(best, availableIntervals[i][1]);
                    ++i;
                }

                if ((best < t) || (best == t && t < e))
                    return -1;

                curr = best;
                ++result;
            }
        }
        
        return result;
    }
};
