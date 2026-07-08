class Solution {
public:
    bool consecutiveSetBits(int n) {
        n = n & (n >> 1);
        return ((n > 0) && !((n & (n-1)) != 0));
    }
};
