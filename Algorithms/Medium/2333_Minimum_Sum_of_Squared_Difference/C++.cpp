class Solution {
public:
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2, int k1, int k2) {
        vector<long long> diffs;
        long long k = k1+k2, total = 0;
        for (int i = 0; i < nums1.size(); ++i) {
            long long num = abs(nums1[i] - nums2[i]);
            diffs.push_back(num);
            total += num;
        }

        if (k >= total)
            return 0;

        sort(diffs.rbegin(), diffs.rend());
        int n = diffs.size();
        long long idx = 0, count = 0;
        while (idx < n) {
            long long curr = diffs[idx];
            while (idx < n && diffs[idx] == curr) {
                ++idx;
                ++count;
            }

            long long next_value = (idx < n) ? diffs[idx] : 0;
            long long needed = (curr - next_value) * count;
            if (k < needed) {
                long long remainder = k % count, value = curr - k/count;
                long long result = (count - remainder) * value * value;
                result += remainder * (value - 1) * (value - 1);
                for (int i = idx; i < n; ++i)
                    result += diffs[i] * diffs[i];

                return result;
            }

            k -= needed;
        }

        return 0;
    }
};
