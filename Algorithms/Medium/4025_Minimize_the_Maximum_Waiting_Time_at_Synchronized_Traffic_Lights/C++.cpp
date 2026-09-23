class Solution {
public:
    int minPenalty(int period, vector<int>& lights, vector<int>& arrivalTime) {
        int result = INT_MAX, max_light = *max_element(lights.begin(), lights.end());
        for (int time : arrivalTime) {
            int r = time % period;
            if (r >= max_light)
                result = min(result, r);
        }

        return (result != INT_MAX) ? period - result : 0;
    }
};
