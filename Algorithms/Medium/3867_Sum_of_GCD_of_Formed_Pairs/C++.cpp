class Solution {
public:
    long long gcdSum(vector<int>& nums) {
        int curr_max = 0;
        vector<int> prefix_gcd;
        for (int num: nums) {
            curr_max = max(curr_max, num);
            prefix_gcd.push_back(gcd(num, curr_max));
        }

        sort(prefix_gcd.begin(), prefix_gcd.end());
        long long result = 0;
        int left = 0, right = nums.size()-1;
        while (left < right)
            result += gcd(prefix_gcd[left++], prefix_gcd[right--]);

        return result;
    }
};
