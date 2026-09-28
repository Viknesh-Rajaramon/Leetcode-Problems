class Solution {
public:
    int minOperations(vector<int>& nums, int sum) {
        vector<int> dp(sum+1, INT_MAX);
        dp[0] = 0;
        for (int num : nums) {
            unordered_map<int, int> costs;
            int value = num, divisions = 0;
            while (value) {
                int current = value, multiplications = 0;
                while (current <= sum) {
                    int cost = divisions + multiplications;
                    if (cost < (costs.count(current) ? costs[current] : INT_MAX))
                        costs[current] = cost;
                    
                    if (current > (sum >> 1))
                        break;
                    
                    current <<= 1;
                    ++multiplications;
                }

                value >>= 1;
                ++divisions;
            }

            vector<int> next_dp(dp.begin(), dp.end());
            for (auto& [value, cost] : costs) {
                for (int current_sum = 0; current_sum <= sum-value; ++current_sum) {
                    if (dp[current_sum] != INT_MAX) {
                        int candidate = dp[current_sum] + cost;
                        if (candidate < next_dp[current_sum + value])
                            next_dp[current_sum + value] = candidate;
                    }
                }
            }

            dp = next_dp;
        }

        return dp[sum] != INT_MAX ? dp[sum] : -1;
    }
};
