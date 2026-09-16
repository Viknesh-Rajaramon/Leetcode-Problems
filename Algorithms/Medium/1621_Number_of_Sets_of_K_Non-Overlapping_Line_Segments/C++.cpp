class Solution {
public:
    int numberOfSets(int n, int k) {
        int mod = 1000000007;
        function<int(int, int)> modPow = [&](int base, int exp) {
            if (exp == 0)
                return 1;

            long long p = modPow(base, exp/2);
            p = (p * p) % mod;
            if (exp%2 == 0)
                return int(p);

            return int((p * (base % mod)) % mod);
        };
            
        function<int(int, int)> nCr = [&](int n, int r) {
            if (r < 0 || r > n)
                return 0;

            if (r == 0 || r == n)
                return 1;

            r = min(r, n-r);
            if (n < mod && r < mod) {
                long long num = 1, den = 1;
                for (int i = 1; i <= r; ++i) {
                    num = (num * (n+1-i)) % mod;
                    den = (den * i) % mod;
                }  

                return int((num * modPow(den, mod-2)) % mod);
            }
            
            return (nCr(n / mod, r / mod) * nCr(n % mod, r % mod)) % mod;
        };

        return nCr(n+k-1, 2*k);
    }
};
