class Solution {
public:
    bool checkGoodInteger(int n) {
        int result = 0;
        while (n > 0 && result < 50) {
            int d = n%10;
            result += d*(d-1);
            n /= 10;
        }

        return result >= 50;
    }
};
