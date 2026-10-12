class Solution {
public:
    vector<int> maxPrimes(int n, int s) {
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

        vector<int> result;
        int total = 0;
        for (int prime = 2; prime <= n; ++prime) {
            if (is_prime[prime]) {
                if (total + prime > s)
                    break;

                total += prime;
                result.push_back(prime);
            }
        }
        
        return result;
    }
};
