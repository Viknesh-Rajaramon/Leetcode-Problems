class Solution {
public:
    int minimumCost(vector<int>& nums, int k) {
        long long result = 0;
        int resources = k, mod = 1000000007;
        for (int num : nums) {
            if (resources < num) {
                int i = (num - resources + k - 1) / k;
                resources += i*k;
                result += i;
            }

            resources -= num;
        }

        return (((result % mod) * ((result + 1) % mod) / 2) % mod);
    }
};
