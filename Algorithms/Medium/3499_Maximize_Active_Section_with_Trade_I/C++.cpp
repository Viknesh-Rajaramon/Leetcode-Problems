class Solution {
public:
    int maxActiveSectionsAfterTrade(string s) {
        int count = 0;
        for (char c: s) {
            if (c == '1')
                ++count;
        }

        int result = 0, prev = INT_MIN, n = s.size(), i = 0;
        while (i < n) {
            int start = i;
            while (i < n && s[i] == s[start])
                ++i;
            
            if (s[start] == '0') {
                int curr = i-start;
                result = max(result, prev+curr);
                prev = curr;
            }
        }

        return result+count;
    }
};
