class Solution {
public:
    int countCommas(int n) {
        int result = 0, divisor = 1000;
        while (n >= divisor) {
            result += n-divisor+1;
            divisor *= 1000;
        }

        return result;
    }
};
