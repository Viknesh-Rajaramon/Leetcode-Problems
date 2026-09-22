class Solution {
public:
    int kthDigit(long long k) {
        if (k < 10)
            return k;
        
        function<long long(long long, long long)> power = [&](long long x, long long n) {
            if (n == 0)
                return 1LL;
            
            long long result = 1;
            while (n > 0) {
                if (n%2 == 1)
                    result *= x;

                x *= x;
                n /= 2;
            }

            return result;
        };
        
        long long d = 1;
        while (k > 9LL * d * pow(10, d-1)) {
            k -= 9LL * d * pow(10, d-1);
            ++d;
        }
            
        
        long long b = pow(10, d-2) + ((k-1)/(10*d)), pos = (k-1) % (10*d);
        long long num_idx = pos / d;
        if (b%2 == 1)
            num_idx = 9 - num_idx;
        
        return int(to_string(10*b + num_idx)[pos % d] - '0');
    }
};
