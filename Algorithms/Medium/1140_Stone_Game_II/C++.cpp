class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int n = piles.size();
        vector<vector<int>> dp(n, vector<int>(n+1));
        vector<int> suffix(n);
        suffix.back() = piles.back();

        for (int i = n-2; i >= 0; --i)
            suffix[i] = suffix[i+1] + piles[i];
        
        for (int i = n-1; i >= 0; --i) {
            for (int j = 1; j <= n; ++j) {
                if (i+2*j >= n)
                    dp[i][j] = suffix[i];
                else
                    for (int k = 1; k <= 2*j; ++k)
                        dp[i][j] = max(dp[i][j], suffix[i] - dp[i+k][max(j, k)]);
            }
        }

        return dp[0][1];
    }
};
