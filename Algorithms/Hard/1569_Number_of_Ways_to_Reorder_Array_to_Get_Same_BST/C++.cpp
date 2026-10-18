class Solution {
public:
    int numOfWays(vector<int>& nums) {
        int mod = 1e9+7, n = nums.size();
        vector<vector<long long>> comb(n+1, vector<long long>(n+1, 0));
        for (int i = 0; i <= n; i++) {
            comb[i][0] = comb[i][i] = 1;
            for (int j = 1; j < i; j++)
                comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % mod;
        }

        function<long long(vector<int>&)> dfs = [&](vector<int>& nums) {
            int n = nums.size();
            if (n <= 2)
                return 1LL;

            vector<int> left, right;
            for (int i = 1; i < n; i++) {
                if (nums[i] < nums[0])
                    left.push_back(nums[i]);
                else
                    right.push_back(nums[i]);
            }

            return (dfs(left) * dfs(right) % mod) * comb[n-1][left.size()] % mod;
        };

        return (dfs(nums) - 1 + mod) % mod;
    }
};
