class Solution {
public:
    int maxEqualAdjacentPairs(vector<int>& nums) {
        int result = 0, n = nums.size(), base = 0;
        map<tuple<int, int>, int> count;
        for (int i = 0; i < n-1; ++i) {
            if (nums[i] == nums[i+1]) {
                ++base;
            } else {
                tuple<int, int> p = {min(nums[i], nums[i+1]), max(nums[i], nums[i+1])};
                ++count[p];
                result = max(result, count[p]);
            }
        }

        return base + result;
    }
};
