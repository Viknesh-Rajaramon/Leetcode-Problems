class Solution {
public:
    int interleaveCharacters(string word1, string word2, string target) {
        int m = word1.length(), n = word2.length(), mod = 1e9+7;
        vector<vector<int>> dp(m+1, vector<int>(n+1));
        dp[m][n] = 1;
        
        for (char c : target) {
            vector<vector<int>> new_dp(m+1, vector<int>(n+1));
            for (int i = 0; i <= m; ++i) {
                int acc = dp[i][n];
                for (int j = 0; j < n; ++j) {
                    if (word2[j] == c)
                        new_dp[i][j] = (new_dp[i][j] + acc) % mod;
                    
                    acc = (acc + dp[i][j]) % mod;
                }
            }

            for (int j = 0; j <= n; ++j) {
                int acc = dp[m][j];
                for (int i = 0; i < m; ++i) {
                    if (word1[i] == c)
                        new_dp[i][j] = (new_dp[i][j] + acc) % mod;
                    
                    acc = (acc + dp[i][j]) % mod;
                }
            }

            dp = new_dp;
        }

        int result = 0;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                result = (result + dp[i][j]) % mod;

        return result;
    }
};
