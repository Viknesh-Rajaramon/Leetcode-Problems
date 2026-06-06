class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        vector<int> result;
        int left_sum = 0, total_sum = 0;
        for (int num : nums) {
            total_sum += num;
        }

        for (int num : nums) {
            left_sum += num;
            result.push_back(abs(total_sum - left_sum));
            total_sum -= num;
        }

        return result;
    }
};
