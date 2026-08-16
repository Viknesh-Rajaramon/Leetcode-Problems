class Solution {
public:
    int longestSubsequence(vector<int>& nums) {
        int result = 0;
        bool all_zero = true;
        for (int num: nums) {
            result ^= num;
            if (num != 0)
                all_zero = false;
        }

        if (all_zero)
            return 0;
        
        return result == 0 ? nums.size()-1 : nums.size();
    }
};
