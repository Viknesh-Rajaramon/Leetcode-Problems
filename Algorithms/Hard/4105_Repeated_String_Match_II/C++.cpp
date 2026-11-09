class Solution {
public:
    bool repeatedStringMatch(string a, string b, int x, int y) {
        int m = a.length(), n = b.length();
        long long ta = 1LL * m * x, tb = 1LL * n * y;
        if (tb > ta)
            return false;
            
        long long temp = min(tb, 1LL * (m * n) / gcd(m, n));
        for (int i = 0; i < m; ++i) {
            if (i + tb > ta)
                break;
            
            bool ok = true;
            for (int j = 0; j < temp; ++j) {
                if (b[j % n] != a[(i+j) % m]) {
                    ok = false;
                    break;
                }
            }

            if (ok)
                return true;
        }

        return false;
    }
};
