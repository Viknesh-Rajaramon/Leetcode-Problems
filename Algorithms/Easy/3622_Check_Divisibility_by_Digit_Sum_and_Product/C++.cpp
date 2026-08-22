class Solution {
public:
    bool checkDivisibility(int n) {
        int sum_ = 0, product_ = 1;
        for (int x = n; x > 0; x /= 10) {
            int r = x % 10;
            sum_ += r;
            product_ *= r;
        }

        return (n % (sum_ + product_) == 0);
    }
};
