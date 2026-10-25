class Solution {
public:
    int peakValleyDifference(vector<int>& nums) {
        int result = 0;
        for (int i = 1; i < nums.size()-1; ++i) {
            if (nums[i] > nums[i-1] && nums[i] > nums[i+1])
                result += nums[i];
            
            if (nums[i] < nums[i-1] && nums[i] < nums[i+1])
                result -= nums[i];
        }
        
        return result;
    }
};
