class Solution {
public:
    vector<int> resultArray(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n);
        result[0] = nums[0];
        result[n-1] = nums[1];
        int idx = 0, rev_idx = n-1;
        for (int i = 2; i < n; ++i) {
            if (result[idx] > result[rev_idx])
                result[++idx] = nums[i];
            else
                result[--rev_idx] = nums[i];
        }

        reverse(result.begin()+rev_idx, result.end());
        return result;
    }
};
