class Solution {
public:
    int resilientSubarray(vector<int>& nums, int k) {
        int result = 1, n = nums.size(), i = 0;
        while (i < n) {
            int r = nums[i]%k, j = i;
            while (j < n && nums[j]%k == r)
                ++j;
            
            int g = k / gcd(r, k);
            result = max(result, 1 + ((j-i-1) / g) * g);
            i = j;
        }
        
        return result;
    }
};
