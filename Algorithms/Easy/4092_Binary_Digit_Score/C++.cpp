class Solution {
public:
    int calculateScore(int a, int b) {
        function<int(int)> bits = [&](int x) {
            int res = 0;
            while (x > 0) {
                res += x%2;
                x >>= 1;
            }
            
            return res;
        };
        
        int s1 = bits(a), s2 = bits(b);
        return s1 >= s2 ? s1 * s2 : s2 / s1;
    }
};
