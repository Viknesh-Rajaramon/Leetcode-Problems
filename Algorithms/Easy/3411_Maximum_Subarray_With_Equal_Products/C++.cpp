class Solution {
public:
    int maxLength(vector<int>& nums) {
        int result = 2, prod = 1, l = 0;
        for (int r = 0; r < nums.size(); ++r) {
            while (gcd(prod, nums[r]) > 1)
                prod /= nums[l++];
            
            prod *= nums[r];
            result = max(result, r-l+1);
        }
        
        return result;
    }
};
