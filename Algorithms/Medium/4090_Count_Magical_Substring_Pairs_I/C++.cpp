class Solution {
public:
    int countMagicalPairs(string s) {
        int result = 0, n = s.length();
        for (int j = 0; j < n-1; ++j) {
            vector<int> r(27);
            unordered_set<char> hs;
            for (int k = j+1; k < n; ++k) {
                hs.insert(s[k]);
                ++r[hs.size()];
            }
            
            hs.clear();
            for (int i = j; i >= 0; --i) {
                hs.insert(s[i]);
                result += r[hs.size()];
            }
        }

        return result;
    }
};
