class Solution {
public:
    long long maxValue(vector<int>& nums) {
        int n = nums.size();
        if (n == 1)
            return nums[0];
        
        long long result = LLONG_MAX, even = nums[0], odd = 0, sum_ = nums[0];
        for (int i = 1; i < n; ++i) {
            if (i%2 == 0) {
                sum_ += nums[i];
                even = max(even, sum_);
                result = min(result, sum_ - even);
            } else {
                sum_ -= nums[i];
                odd = max(odd, sum_);
                result = min(result, sum_ - odd);
            }
        }
        
        return sum_ - 2*result;
    }
};
