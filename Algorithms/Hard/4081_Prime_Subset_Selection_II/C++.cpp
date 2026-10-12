class Solution {
public:
    vector<int> maxPrimeSubset(int n, int s) {
        if (n == 1 or s == 1)
            return {};

        vector<bool> is_prime(n+1, true);
        is_prime[0] = false;
        is_prime[1] = false;
        int i = 2;
        while (i*i <= n) {
            if (is_prime[i]) {
                for (int j = i*i; j <= n; j+= i)
                    is_prime[j] = false;
            }

            ++i;
        }

        vector<int> primes;
        for (int prime = 2; prime <= n; ++prime) {
            if (is_prime[prime])
                primes.push_back(prime);
        }

        n = primes.size();
        vector<vector<int>> dp(n+1, vector<int>(s+1, INT_MAX));
        dp[n][0] = 0;
        for (int i = n-1; i >= 0; --i) {
            for (int t = 0; t <= s; ++t) {
                int best = dp[i+1][t];
                if (t >= primes[i] && dp[i+1][t - primes[i]] != INT_MAX && dp[i+1][t - primes[i]]+1 < best)
                    best = dp[i+1][t - primes[i]]+1;

                dp[i][t] = best;
            }
        }

        int target = 0;
        for (int t = s; t > 0; --t) {
            if (dp[0][t] != INT_MAX) {
                target = t;
                break;
            }
        }

        if (target == 0)
            return {};

        vector<int> result;
        int need = dp[0][target];
        for (int i = 0; i < n; ++i) {
            if (need == 0)
                break;

            if (primes[i] <= target && dp[i+1][target - primes[i]] == need-1) {
                result.push_back(primes[i]);
                target -= primes[i];
                --need;
            }
        }
            
        return result;
    }
};
