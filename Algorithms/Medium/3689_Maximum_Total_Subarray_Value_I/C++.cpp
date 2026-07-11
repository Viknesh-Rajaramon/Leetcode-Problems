class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        int mx = INT_MIN, mn = INT_MAX;
        for (int num: nums) {
            mx = max(mx, num);
            mn = min(mn, num);
        }

        return (long long)(mx-mn) * k;
    }
};
