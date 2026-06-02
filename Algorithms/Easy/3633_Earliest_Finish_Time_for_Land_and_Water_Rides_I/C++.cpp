class Solution {
public:
    int solve(vector<int>& firstStart, vector<int>& firstDur, vector<int>& secondStart, vector<int>& secondDur) {
        int result = INT_MAX, end = INT_MAX;
        for (int i = 0; i < firstStart.size(); ++i)
            end = min(end, firstStart[i] + firstDur[i]);
        
        for (int i = 0; i < secondStart.size(); ++i)
            result = min(result, max(secondStart[i], end) + secondDur[i]);
        
        return result;
    }

    int earliestFinishTime(vector<int>& landStartTime, vector<int>& landDuration, vector<int>& waterStartTime, vector<int>& waterDuration) {
        return min(
            solve(landStartTime, landDuration, waterStartTime, waterDuration),
            solve(waterStartTime, waterDuration, landStartTime, landDuration)
        );
    }
};
