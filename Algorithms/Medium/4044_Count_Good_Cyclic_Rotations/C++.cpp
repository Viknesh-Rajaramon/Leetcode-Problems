class Solution {
public:
    int countGoodRotations(vector<int>& nums) {
        int n = nums.size();
        int result = 0, mid = n/2;
        long long half = 0, total = 0;
        for (int i = 0; i < mid; ++i)
            half += nums[i];
        
        for (int i = 0; i < n; ++i)
            total += nums[i];

        for (int i = 0; i < n; ++i) {
            if (2*half > total)
                ++result;

            half -= nums[i];
            half += nums[(mid+i)%n];
        }

        return result;
    }
};
