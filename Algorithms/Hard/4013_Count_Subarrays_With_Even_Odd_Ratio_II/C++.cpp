class Solution {
public:
    long long countRatioSubarrays(vector<int>& nums, int a, int b) {
        function<int(vector<long long>&, long long)> bisect_right = [&](vector<long long>& arr, long long x) {
            int low = 0, high = arr.size()-1;
            while (low <= high) {
                int mid = (low + high) >> 1;
                if (arr[mid] <= x)
                    low = mid+1;
                else
                    high = mid-1;
            }

            return low;
        };

        long long result = 0, pre = 0;
        vector<long long> x = {0};
        for (int num : nums) {
            pre += ((num%2 == 1) ? a : -b);
            int i = bisect_right(x, pre);
            x.insert(x.begin() + i, pre);
            result += i;
        }

        return result;
    }
};
