class Solution {
public:
    vector<vector<int>> aggregateTimeSeries(vector<vector<int>>& series1, vector<vector<int>>& series2) {
        int m = series1.size(), n = series2.size(), i = 0, j = 0;
        vector<vector<int>> result;
        while (i < m && j < n) {
            if (series1[i][0] == series2[j][0])
                result.push_back(vector<int>{series1[i][0], series1[i++][1] + series2[j++][1]});    
            else if (series1[i][0] < series2[j][0])
                result.push_back(vector<int>{series1[i][0], series1[i++][1] + series2[j][1]});
            else
                result.push_back(vector<int>{series2[j][0], series1[i][1] + series2[j++][1]});
        }
        
        while (i < m)
            result.push_back(series1[i++]);
        
        while (j < n)
            result.push_back(series2[j++]);

        return result;
    }
};
