class Solution {
public:
    int sumDecoded(vector<long long>& nums) {
        int mod = 1e9+7;
        function<long long(long long, long long)> power_mod = [&](long long base, long long exp) {
            long long result = 1;
            while (exp) {
                if (exp & 1)
                    result = ((result % mod) * (base % mod)) % mod;
                
                base = (base * base) % mod;
                exp >>= 1;
            }
            
            return result;
        };

        int result = 0;
        for (long long num : nums) {
            int width = num%10, digits = 0;
            long long d = num/10;
            long long v = d;
            while (v) {
                ++digits;
                v /= 10;
            }
            
            int divisor = 1;
            for (int i = 0; i < digits-width; ++i)
                divisor *= 10;
            
            result = (result + (int)power_mod((d / divisor) % mod, d % divisor)) % mod;
        }

        return result % mod;
    }
};
