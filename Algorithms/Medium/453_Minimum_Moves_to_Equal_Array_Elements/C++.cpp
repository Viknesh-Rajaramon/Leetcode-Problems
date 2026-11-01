class Solution {
public:
    int minMoves(vector<int>& nums) {
        int result = 0, min_ = *min_element(nums.begin(), nums.end());
        for (int num : nums)
            result += num - min_;
        
        return result;
    }
};
