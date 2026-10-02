class Solution {
public:
    int minDays(int n) {
        vector<int> dp(n+1, INT_MAX);
        dp[0] = -1;
        int i = 1;
        while (true) {
            int f = i*(i+1)/2;
            if (f > n)
                break;
            
            for (int j = f; j <= n; ++j)
                dp[j] = min(dp[j], dp[j-f] + i + 1);
            
            ++i;
        }
        
        return dp[n];
    }
};
