class Solution {
public:
    bool winnerSquareGame(int n) {
        vector<bool> dp(n+1);
        for (int i = 1; i <= n; ++i) {
            for (int j = sqrt(i); j > 0; --j) {
                if (!dp[i-j*j]) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[n];
    }
};
