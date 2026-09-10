class Solution {
public:
    int divisibleGame(vector<int>& nums) {
        long long mod = 1e9 + 7;
        int n = nums.size(), max_val = 0;
        vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefix[i+1] = prefix[i] + nums[i];
            max_val = max(max_val, nums[i]);
        }

        if (prefix[n] == n)
            return mod - 2;

        vector<int> spf(max_val+1);
        for (int i = 0; i <= max_val; ++i)
            spf[i] = i;

        for (int i = 2; 1LL * i * i <= max_val; ++i) {
            if (spf[i] == i) {
                for (long long j = 1LL * i * i; j <= max_val; j += i) {
                    if (spf[j] == j)
                        spf[j] = i;
                }
            }
        }

        vector<long long> mix(max_val+1, 0);
        long long max_diff = LLONG_MIN;
        int best_k = 0;
        for (int i = 0; i < n; ++i) {
            int num = nums[i];
            int x = num;
            while (x > 1) {
                int p = spf[x];
                long long diff = max(0LL, mix[p] - prefix[i]) + num;
                if (diff > max_diff || (diff == max_diff && p < best_k)) {
                    max_diff = diff;
                    best_k = p;
                }

                mix[p] = diff + prefix[i+1];
                while (x%p == 0)
                    x /= p;
            }
        }

        return max_diff * best_k % mod;
    }
};
