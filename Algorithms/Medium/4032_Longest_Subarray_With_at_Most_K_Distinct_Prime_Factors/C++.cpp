class Solution {
public:
    int longestSubarray(vector<int>& nums, int k) {
        int M = *max_element(nums.begin(), nums.end());
        vector<int> spf(M+1);
        for (int i = 0; i <= M; ++i)
            spf[i] = i;

        for (int i = 2; i <= int(sqrt(M)); ++i) {
            if (spf[i] == i) {
                for (int j = i*i; j <= M; j += i) {
                    if (spf[j] == j)
                        spf[j] = i;
                }
            }
        }

        function<set<int>(int)> prime_factors = [&](int x) {
            set<int> factors;
            while (x > 1) {
                int p = spf[x];
                factors.insert(p);
                while (x % p == 0)
                    x /= p;
            }

            return factors;
        };

        int result = 0, l = 0;
        unordered_map<int, int> freq;
        for (int r = 0; r < nums.size(); ++r) {
            for (int p : prime_factors(nums[r]))
                freq[p] = (freq.find(p) != freq.end() ? freq[p] : 0) + 1;

            while (freq.size() > k) {
                for (int p : prime_factors(nums[l])) {
                    --freq[p];
                    if (freq[p] == 0)
                        freq.erase(p);
                }

                ++l;
            }

            result = max(result, r - l + 1);
        }   
        
        return result;
    }
};
