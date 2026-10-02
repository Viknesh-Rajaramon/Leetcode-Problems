class Solution {
public:
    long long result, k1, k2;
    vector<long long> a, temp;
    void ff(int low, int high) {
        if (low >= high)
            return;

        int mid = (low+high) >> 1;
        ff(low, mid);
        ff(mid+1, high);
        int p1 = mid+1, p2 = mid+1;
        for (int i = low; i <= mid; ++i) {
            while (p1 <= high && a[p1] < a[i] + k1)
                ++p1;

            while (p2 <= high && a[p2] <= a[i] + k2)
                ++p2;

            result -= p2 - p1;
        }

        int i = low, j = mid+1, p = low;
        while (i <= mid && j <= high) {
            if (a[i] <= a[j])
                temp[p++] = a[i++];
            else
                temp[p++] = a[j++];
        }

        while (i <= mid)
            temp[p++] = a[i++];

        while (j <= high)
            temp[p++] = a[j++];

        for (p = low; p <= high; ++p)
            a[p] = temp[p];
    }

    long long distantSubarrays(vector<int>& nums, int goal, int k) {
        int n = nums.size();
        result = 1LL * n * (n + 1) / 2;
        if (k == 0)
            return result;

        a.resize(n + 1);
        temp.resize(n + 1);
        long long prefix = 0;
        for (int i = 0; i < n; i++) {
            prefix += nums[i];
            a[i+1] = prefix;
        }

        k1 = goal-k+1;
        k2 = goal+k-1;
        ff(0, n);
        return result;
    }
};
