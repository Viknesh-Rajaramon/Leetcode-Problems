class Solution {
public:
    int maxPalindromes(string s, int k) {
        function<bool(int, int)> check = [&](int l, int r) {
            while (l < r) {
                if (s[l++] != s[r--])
                    return false;
            }

            return true;
        };

        int result = 0, n = s.length(), start = 0;
        for (int r = k-1; r < n; ++r) {
            int l = r-k+1;
            if (l >= start && check(l, r)) {
                ++result;
                start = r+1;
                continue;
            }

            l = r-k;
            if (l >= start && check(l, r)) {
                ++result;
                start = r+1;
            }
        }

        return result;
    }
};
