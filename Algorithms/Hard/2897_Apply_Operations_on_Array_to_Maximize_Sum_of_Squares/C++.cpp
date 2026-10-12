class Solution {
public:
    int maxSum(vector<int>& nums, int k) {
        int mod = 1e9+7;
        vector<int> count(30);
        for (int num : nums) {
            for (int i = 0; i < 30; ++i) {
                if (num & (1 << i))
                    ++count[i];
            }
        }
        
        int result = 0;
        for (int i = 0; i < k; ++i) {
            int curr = 0;
            for (int j = 29; j >= 0; --j) {
                if (count[j] == 0)
                    continue;
                
                curr |= 1 << j;
                --count[j];
            }
            
            result = (result + ((1LL * curr * curr) % mod)) % mod;
        }

        return result;
    }
};
