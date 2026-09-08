class Solution {
public:
    int countValidSubarrays(vector<int>& nums, int x) {
        int result = 0, n = nums.size();
        vector<long long> prefix(n+1);
        for (int i = 0; i < n; ++i)
            prefix[i+1] = prefix[i] + nums[i];
        
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) {
                long long total = prefix[j+1] - prefix[i];
                if (total % 10 != x)
                    continue;

                while (total >= 10)
                    total /= 10;
                
                if (total == x)
                    ++result;
            }
        }

        return result;
    }
};
