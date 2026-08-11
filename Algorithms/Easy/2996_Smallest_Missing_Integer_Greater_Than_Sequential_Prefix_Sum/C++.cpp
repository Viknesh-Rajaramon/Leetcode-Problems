class Solution {
public:
    int missingInteger(vector<int>& nums) {
        int result = nums[0], i = 1;
        while (i < nums.size() && nums[i] == nums[i-1]+1)
            result += nums[i++];
        
        set<int> num_set(nums.begin(), nums.end());
        while (num_set.find(result) != num_set.end())
            ++result;
        
        return result;
    }
};
