class Solution {
public:
    int maxValidSplits(vector<int>& nums) {
        function<int(vector<int>&)> score = [&](vector<int>& arr) {
            int m = arr.size();
            if (m == 1)
                return 0;
            
            vector<int> suffix(m);
            suffix[m-1] = arr[m-1];
            for (int i = m-2; i >= 0; --i)
                suffix[i] = gcd(suffix[i+1], arr[i]);
            
            int ans = 0, left_gcd = 0;
            for (int i = 0; i < m-1; ++i) {
                left_gcd = gcd(left_gcd, arr[i]);
                if (left_gcd == suffix[i+1])
                    ++ans;
            }

            return ans;
        };

        int result = score(nums), n = nums.size();
        if (n <= 2)
            return result;

        int g = 0;
        for (int i = 0; i < n; ++i) {
            if (i > 0 && gcd(g, nums[i]) != g) {
                vector<int> arr(nums.begin(), nums.begin() + i);
                arr.insert(arr.end(), nums.begin()+i+1, nums.end());
                result = max(result, score(arr));
            }
            
            g = gcd(g, nums[i]);
        }
        
        g = 0;
        for (int i = n-1; i >= 0; --i) {
            if (i < n-1 && gcd(g, nums[i]) != g) {
                vector<int> arr(nums.begin(), nums.begin() + i);
                arr.insert(arr.end(), nums.begin()+i+1, nums.end());
                result = max(result, score(arr));
            }
            
            g = gcd(g, nums[i]);
        }
            
        
        return result;
    }
};
