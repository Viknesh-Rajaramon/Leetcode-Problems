class Solution {
public:
    long long maxRatings(vector<vector<int>>& units) {
        int n = units[0].size(), global_min = INT_MAX, sec_min = INT_MAX;
        long long result = 0;
        for (auto& it : units) {
            sort(it.begin(), it.end());
            global_min = min(global_min, it[0]);
            if (n > 1) {
                sec_min = min(sec_min, it[1]);
                result += it[1];
            } else {
                sec_min = min(sec_min, it[0]);
                result += it[0];
            }
        }

        return (result - sec_min + global_min);
    }
};
