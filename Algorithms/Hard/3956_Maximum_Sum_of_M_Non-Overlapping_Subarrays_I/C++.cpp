class Solution {
public:
    long long maximumSum(vector<int>& nums, int m, int l, int r) {
        int n = nums.size();
        vector<long long> prefix(n+1);
        for (int i = 0; i < n; ++i)
            prefix[i+1] = prefix[i] + nums[i];

        long long result = LLONG_MIN;
        vector<long long> dp(n+1);
        for (int i = 1; i <= m; ++i) {
            deque<pair<long long, int>> queue;
            vector<long long> new_dp(n+1, LLONG_MIN);

            for (int j = l*i; j <= n; ++j) {
                int k = j-l;
                long long curr_val = dp[k] - prefix[k];
                while (!queue.empty() && queue.back().first <= curr_val)
                    queue.pop_back();
                
                queue.push_back({curr_val, k});
                if (queue.front().second < j-r)
                    queue.pop_front();
                
                new_dp[j] = max(new_dp[j-1], queue.front().first+prefix[j]);
            }

            result = max(result, new_dp[n]);
            dp = new_dp;
        }

        return result;
    }
};
