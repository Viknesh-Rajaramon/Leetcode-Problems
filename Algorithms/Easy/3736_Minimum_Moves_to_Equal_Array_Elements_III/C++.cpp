class Solution {
public:
    int minMoves(vector<int>& nums) {
        int result = 0, max_ = *max_element(nums.begin(), nums.end());
        for (int num : nums)
            result += max_ - num;
        
        return result;
    }
};
