class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size(), ind_0 = 0;
        for (int i = 0; i < n; ++i) {
            if (nums[i] == 0) {
                ind_0 = i;
                break;
            }
        }

        bool result = true;
        for (int i = ind_0; i < ind_0+n-1; ++i) {
            if (nums[i%n] >= nums[(i+1)%n]) {
                result = false;
                break;
            }
        }

        if (result)
            return min(ind_0, n + 2 - ind_0);

        result = true;
        for (int i = ind_0; i > ind_0-n+1; --i) {
            if (nums[(n+i)%n] >= nums[(n+i-1)%n]) {
                result = false;
                break;
            }
        }

        if (result)
            return min(n - ind_0, 2 + ind_0);
        
        return -1;
    }
};
