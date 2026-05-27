class Solution {
public:
    int numberOfSpecialChars(string word) {
        vector<int> lower(26, -1), upper(26, -1);
        for (int i = 0; i < word.size(); ++i) {
            if (word[i] >= 'a' && word[i] <= 'z')
                lower[word[i]-97] = i;
            else if (upper[word[i]-65] == -1)
                upper[word[i]-65] = i;
        }

        int result = 0;
        for (int i = 0; i < 26; ++i) {
            if (lower[i] != -1 && lower[i] < upper[i])
                ++result;
        }

        return result;
    }
};
