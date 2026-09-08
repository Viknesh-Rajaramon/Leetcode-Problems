class Solution {
public:
    long long dp[20][12][2][2];

    long long dfs(int i, int p, bool tight, bool started, string s, int k) {
        if (i == s.length())
            return started ? 1 : 0;
        
        if (dp[i][p+1][tight][started] != -1)
            return dp[i][p+1][tight][started];

        long long result = 0;
        int limit = tight ? s[i]-'0' : 9;
        for (int d = 0; d <= limit; ++d) {
            if (p == -1 && d == 0)
                result += dfs(i+1, -1, tight && (d == limit), false, s, k);
            else if (p == -1 || abs(p-d) <= k)
                result += dfs(i+1, d, tight && (d == limit), true, s, k);
        }

        dp[i][p+1][tight][started] = result;
        return result;
    }

    long long solve(long long num, int k) {
        memset(dp, -1, sizeof(dp));
        string s = to_string(num);
        return dfs(0, -1, true, false, s, k);
    }

    long long goodIntegers(long long l, long long r, int k) {
        return solve(r, k) - solve(l-1, k);
    }
};
