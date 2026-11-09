class Solution {
public:
    int countSuffix(vector<int>& nums, vector<int>& target) {
        int n = nums.size(), i = 0;
        bool ok = true;
        for (i = 0; i < n; ++i) {
            if (nums[i] != target[i]) {
                ok = false;
                break;
            }
        }

        if (ok)
            i = n-1;

        sort(nums.begin() + i, nums.end(), greater<int>());
        if (nums != target)
            return 0;

        int result = 1;
        for (int j = i-1; j >= 0; --j) {
            if (target[j] < target[j+1])
                break;

            ++result;
        }

        return result;
    }
};
