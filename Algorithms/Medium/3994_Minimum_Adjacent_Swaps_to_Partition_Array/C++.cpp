class Solution {
public:
    int minAdjacentSwaps(vector<int>& nums, int a, int b) {
        int result = 0, count_1 = 0, count_2 = 0, mod = 1000000007;
        for (int num : nums) {
            if (num < a) {
                result = (result + (count_1 + count_2) % mod) % mod;
            } else if (num > b) {
                count_2 = (count_2 + 1) % mod;
            } else {
                count_1 = (count_1 + 1) % mod;
                result = (result + count_2) % mod;
            }
        }
        
        return result;
    }
};
