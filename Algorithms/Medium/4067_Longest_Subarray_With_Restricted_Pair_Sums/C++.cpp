class Solution {
public:
    int maxSubarray(vector<int>& nums) {
        int result = 0, n = nums.size(), l = 0;
        vector<int> count(501);
        function<bool(int)> is_valid = [&](int target) {
            for (int i = 1; i <= target/2; ++i) {
                if (2*i == target) {
                    if (count[i] >= 2)
                        return false;
                } else {
                    if (count[i] > 0 && count[target-i] > 0)
                        return false;
                }
            }
            
            for (int i = 1; i < 501-target; ++i)
                if (count[i] > 0 && count[i+target] > 0)
                    return false;
            
            return true;
        };

        for (int r = 0; r < n; ++r) {
            while (!is_valid(nums[r]))
                --count[nums[l++]];
            
            ++count[nums[r]];
            result = max(result, r-l+1);
        }
        
        return result;
    }
};
