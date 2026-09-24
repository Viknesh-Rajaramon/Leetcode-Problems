class Solution {
public:
    int smallestIndex(vector<int>& nums) {
        function<int(int)> sum_of_digits = [&](int num) {
            int result = 0;
            while (num > 0) {
                result += num % 10;
                num /= 10;
            }
            
            return result;
        };

        for (int i = 0; i < nums.size(); ++i) {
            if (i == sum_of_digits(nums[i]))
                return i;
        }

        return -1;
    }
};
