class Solution {
public:
    vector<int> maximumMEX(vector<int>& nums) {
        int n = nums.size(), mx = 100002, mex = 0, curr_mex = 0;
        vector<int> total_cnt(mx), curr_cnt(mx);
        for (int num : nums)
            ++total_cnt[num];
        
        while (total_cnt[mex] > 0)
            ++mex;
        
        vector<int> result;
        int l = 0;
        for (int r = 0; r < n; ++r) {
            ++curr_cnt[nums[r]];
            while (curr_cnt[curr_mex] > 0)
                ++curr_mex;
            
            if (curr_mex == mex) {
                result.push_back(mex);
                for (int i = l; i <= r; ++i) {
                    --total_cnt[nums[i]];
                    --curr_cnt[nums[i]];
                    if (total_cnt[nums[i]] == 0)
                        mex = min(mex, nums[i]);
                }

                curr_mex = 0;
                l = r+1;
            }
        }

        return result;
    }
};
