class Solution {
public:
    long long maxPairStrength(vector<int>& nums) {
        function<int(int, int)> gcd = [&](int a, int b) {
            while (b != 0) {
                int temp = a;
                a = b;
                b = temp%b;
            }

            return a;
        };
        
        long long result = 0;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i+1; j < n; ++j) {
                int g = gcd(nums[i], nums[j]);
                result = max(result, (1LL * nums[i] * nums[j]) / (1LL * g * g));
            }
        }

        return result;
    }
};
