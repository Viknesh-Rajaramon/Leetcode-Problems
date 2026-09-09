class Solution {
public:
    vector<vector<int>> filterOccupiedIntervals(vector<vector<int>>& occupiedIntervals, int freeStart, int freeEnd) {
        sort(occupiedIntervals.begin(), occupiedIntervals.end());
        int idx = 0;
        for (int i = 0; i < occupiedIntervals.size(); ++i) {
            if (occupiedIntervals[i][0] <= occupiedIntervals[idx][1]+1)
                occupiedIntervals[idx][1] = max(occupiedIntervals[idx][1], occupiedIntervals[i][1]);
            else
                occupiedIntervals[++idx] = occupiedIntervals[i];
        }
        
        vector<vector<int>> result;
        for (int i = 0; i <= idx; ++i) {
            int start = occupiedIntervals[i][0], end = occupiedIntervals[i][1];
            if (end < freeStart || start > freeEnd)
                result.push_back({start, end});

            if (start < freeStart && end >= freeStart)
                result.push_back({start, freeStart-1});

            if (start <= freeEnd && end > freeEnd)
                result.push_back({freeEnd+1, end});
        }

        return result;
    }
};
