class Solution {
public:
    int numDistinct(string s, string t) {
        int m = s.length(), n = t.length();
        vector<unsigned long long> dp(n+1);
        dp[n] = 1;
        for (int i = m-1; i >= 0; --i) {
            int start = max(0, n-m+i), end = min(n-1, i);
            for (int j = start; j <= end; ++j)
                if (s[i] == t[j])
                    dp[j] += dp[j+1];
        }

        return dp[0];
    }
};
