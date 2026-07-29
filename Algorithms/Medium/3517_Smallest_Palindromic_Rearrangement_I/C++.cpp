class Solution {
public:
    string smallestPalindrome(string s) {
        vector<char> result;
        int n = s.size();
        unordered_map<char, int> counter;
        for (int i = 0; i < n/2; ++i)
            counter[s[i]]++;

        for (int i = 0; i < 26; ++i) {
            char c = 'a' + i;
            for (int j = 0; j < counter[c]; ++j)
                result.push_back(c);
        }

        if (n%2 == 1)
            result.push_back(s[n/2]);

        for (int i = 25; i >= 0; --i) {
            char c = 'a' + i;
            for (int j = 0; j < counter[c]; ++j)
                result.push_back(c);
        }

        return string(result.begin(), result.end());
    }
};
