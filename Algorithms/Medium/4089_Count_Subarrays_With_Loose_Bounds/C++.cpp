class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        long long result = 0;
        int l = 0;
        for (int r = 0; r < nums.size(); ++r) {
            if (nums[r] < minK || nums[r] > maxK)
                l = r+1;
            else
                result += r-l+1;
        }

        return result;
    }
};
