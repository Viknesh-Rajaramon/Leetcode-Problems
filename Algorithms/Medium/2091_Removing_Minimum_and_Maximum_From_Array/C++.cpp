class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int n = nums.size(), min_idx = 0, max_idx = 0;
        for (int i = 0; i < n; ++i) {
            if (nums[i] < nums[min_idx])
                min_idx = i;
            
            if (nums[i] > nums[max_idx])
                max_idx = i;
        }

        int l = min(min_idx, max_idx), r = max(min_idx, max_idx);
        return min(min(r+1, n-l), l+1+n-r);
    }
};
