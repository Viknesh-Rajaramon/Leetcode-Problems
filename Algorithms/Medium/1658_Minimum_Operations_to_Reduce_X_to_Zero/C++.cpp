class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int n = nums.size(), target = -x;
        for (int num : nums)
            target += num;

        if (target < 0)
            return -1;
        
        int result = -1, l = 0, curr_sum = 0;
        for (int r = 0; r < n; ++r) {
            curr_sum += nums[r];
            while (curr_sum > target)
                curr_sum -= nums[l++];
            
            if (curr_sum == target)
                result = max(result, r-l+1);
        }

        return result != -1 ? n - result : -1;
    }
};
