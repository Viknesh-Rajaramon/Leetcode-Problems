class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) {
        int n = nums.size(), min_element = INT_MAX, max_ = 0;
        vector<int> min_(n);
        for (int i = n-1; i >= 0; --i) {
            min_element = min(min_element, nums[i]);
            min_[i] = min_element;
        }
        
        for (int i = 0; i < n; ++i) {
            max_ = max(max_, nums[i]);
            if (max_ - min_[i] <= k)
                return i;
        }
        
        return -1;
    }
};
