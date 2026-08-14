class Solution {
public:
    int maximumLengthSubstring(string s) {
        int result = 0, l = 0;
        vector<int> count(26);
        for (int r = 0; r < s.size(); ++r) {
            char c = s[r] - 'a';
            ++count[c];
            while (count[c] > 2)
                --count[s[l++]-'a'];

            result = max(result, r-l+1);
        }

        return result;
    }
};
