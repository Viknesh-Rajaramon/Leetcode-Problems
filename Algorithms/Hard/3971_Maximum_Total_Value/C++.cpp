class Solution {
public:
    bool is_valid(int x, vector<int>& value, vector<int>& decay, int m) {
        long long count = 0;
        for (int i = 0; i < value.size(); ++i) {
            if (value[i] >= x)
                count += ((value[i] - x) / decay[i]) + 1;
        }

        return (count >= m);
    }

    int maxTotalValue(vector<int>& value, vector<int>& decay, int m) {
        int mod = 1e9+7, n = value.size(), low = 1, high = 1;
        for (int val : value)
            high = max(high, val);
        
        while (low <= high) {
            int mid = (low+high) >> 1;
            if (is_valid(mid, value, decay, m))
                low = mid+1;
            else
                high = mid-1;
        }

        long long result = 0, count = 0;
        int threshold = high;
        for (int i = 0; i < n; ++i) {
            if (value[i] < threshold)
                continue;
            
            long long t = (value[i] - threshold) / decay[i] + 1;
            count += t;
            result = (result + ((t * (2*value[i] - (t-1)*decay[i]) / 2) % mod)) % mod;
        }

        result = (result + (threshold*(m - count) % mod)) % mod;
        return result >= 0 ? result : result+mod;
    }
};
