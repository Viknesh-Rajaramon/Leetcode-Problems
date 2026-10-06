class Solution {
public:
    int countGoodStrings(long long n) {
        int mod = 1e9+7;
        function<vector<long long>(long long)> fib = [&](long long k) {
            if (k == 0)
                return vector<long long>{0, 1};

            vector<long long> f = fib(k >> 1);
            long long c = f[0] * ((2*f[1] - f[0] + mod) % mod) % mod;
            long long d = ((f[0] * f[0] % mod) + (f[1] * f[1] % mod)) % mod;
            if ((k & 1) != 0)
                return vector<long long>{d, (c+d) % mod};

            return vector<long long>{c, d};
        };
            
        return (2 * fib(n)[0]) % mod;
    }
};
