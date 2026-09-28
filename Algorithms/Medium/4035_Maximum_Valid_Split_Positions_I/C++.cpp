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

        int result = score(nums);
        for (int i = 0; i < nums.size(); ++i) {
            vector<int> arr(nums.begin(), nums.begin() + i);
            arr.insert(arr.end(), nums.begin()+i+1, nums.end());
            result = max(result, score(arr));
        }
        
        return result;
    }
};
