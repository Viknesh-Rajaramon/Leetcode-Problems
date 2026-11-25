class Solution {
public:
    int smallestUniqueSubarray(vector<int>& nums) {
        long long MOD = 1000000007LL, BASE = 911382323LL;
        int n = nums.size();
        vector<long long> h(n+1), p(n+1);
        p[0] = 1;

        for (int i = 0; i < n; ++i) {
            h[i+1] = (h[i] * BASE + nums[i]) % MOD;
            p[i+1] = p[i] * BASE % MOD;
        }

        auto check = [&](int len) {
            unordered_map<long long, int> cnt;
            for (int l = 0; l+len <= n; ++l) {
                long long key = (h[l+len] - h[l] * p[len] % MOD + MOD) % MOD;
                ++cnt[key];
            }

            for (auto& [_, times] : cnt) {
                if (times == 1)
                    return true;
            }

            return false;
        };

        int low = 1, high = n;
        while (low < high) {
            int mid = (low+high) >> 1;
            if (check(mid))
                high = mid;
            else
                low = mid+1;
        }

        return low;
    }
};
