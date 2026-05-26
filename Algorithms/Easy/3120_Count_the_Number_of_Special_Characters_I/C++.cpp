class Solution {
public:
    int numberOfSpecialChars(string word) {
        vector<bool> lower(26, false), upper(26, false);
        for (auto c : word) {
            if (islower(c))
                lower[c-'a'] = true;
            else
                upper[c-'A'] = true;
        }

        int result = 0;
        for (int i = 0; i < 26; ++i) {
            if (lower[i] && upper[i])
                ++result;
        }

        return result;
    }
};
