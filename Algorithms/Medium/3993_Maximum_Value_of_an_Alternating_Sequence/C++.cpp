class Solution {
public:
    long long maximumValue(int n, int s, int m) {
        if (n == 1)
            return s;

        return s + 1LL*(n/2)*(m-1) + 1;
    }
};
