class Solution {
public:
    int minOperations(string s) {
        int result = INT_MAX, n = s.length();
        for (int k = 0; k < n; ++k) {
            int ops = k;
            for (int i = 0; i < n/2; ++i) {
                int inc = abs(int(s[(k+i) % n] - 'a') - int(s[(n+k-1-i) % n] - 'a'));
                ops += min(inc, 26 - inc);
            }

            result = min(result, ops);
        }

        return result;
    }
};
