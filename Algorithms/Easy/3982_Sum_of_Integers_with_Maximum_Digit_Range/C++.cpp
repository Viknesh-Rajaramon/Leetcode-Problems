class Solution {
public:
    int maxDigitRange(vector<int>& nums) {
        int result = 0, max_digit_range = 0;
        for (int num : nums) {
            int largest = 0, smallest = 10, x = num;
            while (x > 0) {
                int d = x%10;
                largest = max(largest, d);
                smallest = min(smallest, d);
                x /= 10;
            }

            if (largest-smallest > max_digit_range) {
                result = num;
                max_digit_range = largest-smallest;
            } else if (largest-smallest == max_digit_range) {
                result += num;
            }
        }

        return result;
    }
};
