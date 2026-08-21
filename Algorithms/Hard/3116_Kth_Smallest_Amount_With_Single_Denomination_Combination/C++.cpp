class Solution {
public:
    long long findKthSmallest(vector<int>& coins, int k) {
        sort(coins.begin(), coins.end());
        vector<int> new_coins;
        for (int i = 0; i < coins.size(); ++i) {
            bool is_valid = true;
            for (int j = 0; j < i; ++j) {
                if (coins[i] % coins[j] == 0) {
                    is_valid = false;
                    break;
                }
            }

            if (is_valid)
                new_coins.push_back(coins[i]);
        }

        int n = 1 << new_coins.size();
        long long left = k, right = 1ll * new_coins[0]*k+1;
        vector<long long> lcm(n, 1);
        for (int mask = 1; mask < n; ++mask) {
            int pre_mask = mask & (mask-1);
            int i = __builtin_ctz(mask);
            long long tmp = lcm[pre_mask] / gcd(lcm[pre_mask], new_coins[i]);
            lcm[mask] = tmp <= right / new_coins[i] ? tmp*new_coins[i] : right+1;
        }

        function<long long(long long)> get = [&](long long x) {
            long long count = 0;
            for (int mask = 1; mask < n; ++mask) {
                if (lcm[mask] > x)
                    continue;
                
                if (__builtin_popcount(mask) & 1)
                    count += x/lcm[mask];
                else
                    count -= x/lcm[mask];
            }

            return count;
        };

        while (left < right) {
            long long mid = (left+right) >> 1;
            if (get(mid) >= k)
                right = mid;
            else
                left = mid+1;
        }

        return left;
    }
};
