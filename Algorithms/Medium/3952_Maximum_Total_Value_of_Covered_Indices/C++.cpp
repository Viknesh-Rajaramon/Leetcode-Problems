class Solution {
public:
    long long maxTotal(vector<int>& nums, string s) {
        long long prev = 0, curr = s[0] == '1' ? nums[0] : 0;
        for (int i = 1; i < nums.size(); ++i) {
            if (s[i] == '1') {
                prev += nums[i-1];
                curr = max(curr+nums[i], prev);
            } else {
                prev = curr;
            }
        }

        return curr;
    }
};
