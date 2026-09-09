class Solution {
public:
    long long solve(bool mul, vector<int>& nums, int k) {
		long long result = LLONG_MIN, dp_0 = LLONG_MIN, dp_1 = LLONG_MIN, dp_2 = LLONG_MIN;
		for (int num : nums) {
            long long y;
			if (mul)
				y = 1LL * num * k;
			else
				y = (num >= 0) ? (num/k) : -((-num) / k);

			long long d_0 = num, d_1 = y, d_2 = LLONG_MIN;
			if (dp_0 != LLONG_MIN) {
				d_0 = max(d_0, dp_0 + num);
				d_1 = max(d_1, dp_0 + y);
			}

			if (dp_1 != LLONG_MIN) {
				d_1 = max(d_1, dp_1 + y);
				d_2 = max(d_2, dp_1 + num);
			}

			if (dp_2 != LLONG_MIN)
				d_2 = max(d_2, dp_2 + num);

			dp_0 = d_0;
            dp_1 = d_1;
            dp_2 = d_2;
			result = max({result, dp_1, dp_2});
		}

		return result;
	}

    long long maxSubarraySum(vector<int>& nums, int k) {
        return max(solve(true, nums, k), solve(false, nums, k));
    }
};
