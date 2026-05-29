class Solution {
public:
    int minElement(vector<int>& nums) {
        int result = 9+9+9+9;
        for (int num : nums) {
            int sum = 0;
            while (num > 0) {
                sum += num%10;
                num /= 10;
            }

            if (sum < result)
                result = sum;
        }

        return result;
    }
};
