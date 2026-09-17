class Solution {
public:
    int minSumOfLengths(vector<int>& arr, int target) {
        int result = arr.size()+1, n = arr.size(), total = 0, l = 0;
        vector<int> dp(n+1, n);
        for (int r = 0; r < n; ++r) {
            total += arr[r];
            while (total > target)
                total -= arr[l++];
            
            dp[r+1] = dp[r];
            if (total == target) {
                result = min(result, r-l+1+dp[l]);
                dp[r+1] = min(dp[r], r-l+1);
            }
        }
        
        return result != n+1 ? result : -1;
    }
};
