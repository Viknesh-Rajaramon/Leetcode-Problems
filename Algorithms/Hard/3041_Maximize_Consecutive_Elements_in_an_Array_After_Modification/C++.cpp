class Solution {
public:
    int maxSelectedElements(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int result = 0;
        unordered_map<int, int> dp;
        for (int num : nums) {
            dp[num+1] = dp[num]+1;
            dp[num] = dp[num-1]+1;
            result = max({result, dp[num+1], dp[num]});
        }

        return result;
    }
};
