class Solution {
public:
    int secondsBetweenTimes(string startTime, string endTime) {
        auto f = [&](char c) {
            return int(c - '0');
        };

        auto diff = [&](int i) {
            return 10*(f(endTime[i]) - f(startTime[i])) + f(endTime[i+1]) - f(startTime[i+1]);
        };

        return 60*(60*(diff(0)) + diff(3)) + diff(6);
    }
};
