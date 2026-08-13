class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        int result = 0, l = 0;
        map<int, int> freq;
        for (int r = 0; r < nums.size(); ++r) {
            ++freq[nums[r]];
            while (freq[nums[r]] > k)
                --freq[nums[l++]];
            
            result = max(result, r-l+1);
        }

        return result;
    }
};
