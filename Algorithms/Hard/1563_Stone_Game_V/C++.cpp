class Solution {
public:
    int stoneGameV(vector<int>& stoneValue) {
        int n = stoneValue.size();
        vector<vector<int>> dp(n, vector<int>(n)), left(n, vector<int>(n)), right(n, vector<int>(n));
        for (int i = 0; i < n; ++i) {
            left[i][i] = stoneValue[i];
            right[i][i] = stoneValue[i];
        }

        for (int start = n-2; start >= 0; --start) {
            int total_sum = stoneValue[start], split_at = start, left_sum = 0;
            for (int end = start+1; end < n; ++end) {
                total_sum += stoneValue[end];
                while (split_at <= end && 2*(left_sum+stoneValue[split_at]) <= total_sum)
                    left_sum += stoneValue[split_at++];
                
                if (2*left_sum == total_sum) {
                    dp[start][end] = max(left[start][split_at-1], right[split_at][end]);
                } else {
                    if (start == split_at)
                        dp[start][end] = split_at+1 <= end ? right[split_at+1][end] : 0;
                    else
                        dp[start][end] = max(
                            split_at-1 >= start ? left[start][split_at-1] : 0,
                            split_at+1 <= end ? right[split_at+1][end] : 0
                        );
                }

                left[start][end] = max(left[start][end-1], total_sum + dp[start][end]);
                right[start][end] = max(right[start+1][end], total_sum + dp[start][end]);
            }
        }

        return dp[0].back();
    }
};
