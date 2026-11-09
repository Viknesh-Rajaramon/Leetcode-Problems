class Solution {
public:
    vector<vector<string>> findMismatchedSegments(string s1, string s2) {
        vector<vector<string>> result;
        int n = s1.length(), i = 0;
        while (i < n) {
            if (s1[i] == s2[i]) {
                ++i;
                continue;
            }

            int start = i;
            while (i < n && s1[i] != s2[i])
                ++i;
            
            result.push_back({s1.substr(start, i-start), s2.substr(start, i-start)});
        }

        return result;
    }
};
