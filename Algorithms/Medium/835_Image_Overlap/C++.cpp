class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        int n = img1.size();
        vector<pair<int, int>> img1_points, img2_points;
        map<pair<int, int>, int> d;
        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < n; ++c) {
                if (img1[r][c] == 1)
                    img1_points.push_back({r, c});
                
                if (img2[r][c] == 1)
                    img2_points.push_back({r, c});
            }
        }

        for (const auto& [ra, ca] : img1_points) {
            for (const auto& [rb, cb] : img2_points) {
                pair<int, int> key = {rb - ra, cb - ca};
                if (d.find(key) == d.end())
                    d.insert({key, 0});

                ++d[key];
            }
        }

        int result = 0;
        for (const auto& [_, val] : d)
            result = max(result, val);

        return result;
    }
};
