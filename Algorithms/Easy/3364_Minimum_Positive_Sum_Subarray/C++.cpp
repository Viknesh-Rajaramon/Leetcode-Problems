class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int n = nums.size();
        vector<int> prefix_sum(n+1);
        for (int i = 0; i < n; ++i)
            prefix_sum[i+1] = prefix_sum[i] + nums[i];
        
        int result = INT_MAX;
        for (int length = l; length <= min(r, n); ++length) {
            for (int start = 0; start <= n-length; ++start) {
                int total = prefix_sum[start+length] - prefix_sum[start];
                if (total > 0)
                    result = min(result, total);
            }
        }                    

        return result != INT_MAX ? result : -1;
    }
};
