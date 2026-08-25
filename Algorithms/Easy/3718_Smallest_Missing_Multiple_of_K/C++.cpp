class Solution {
public:
    int missingMultiple(vector<int>& nums, int k) {
        set<int> seen(nums.begin(), nums.end());
        int result = k;
        while (seen.find(result) != seen.end())
            result += k;

        return result;
    }
};
