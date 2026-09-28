class Solution {
public:
    int countSpecialIntegers(vector<int>& nums) {
        unordered_map<int, int> first, last, freq;
        for (int i = 0; i < nums.size(); ++i) {
            if (!first.count(nums[i])) {
                first[nums[i]] = i;
                freq[nums[i]] = 0;
            }
            
            last[nums[i]] = i;
            ++freq[nums[i]];
        }
        
        int result = 0;
        for (auto& [num, _] : freq)
            if (last[num] - first[num] + 1 == freq[num])
                ++result;

        return result;
    }
};
