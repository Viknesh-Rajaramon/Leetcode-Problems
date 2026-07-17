class Solution {
public:
    vector<int> gcdValues(vector<int>& nums, vector<long long>& queries) {
        int mx = *max_element(nums.begin(), nums.end());
        vector<long long> freq(mx+1), count(mx+1);
        for (int num: nums)
            ++freq[num];
        
        for (int g = mx; g > 0; --g) {
            long long total = 0;
            for (int m = g; m <= mx; m += g)
                total += freq[m];
            
            long long pairs = total*(total-1)/2;
            for (int m = 2*g; m <= mx; m += g)
                pairs -= count[m];
            
            count[g] = pairs;
        }

        vector<long long> pref;
        vector<int> vals;
        long long s = 0;
        for (int g = 1; g <= mx; ++g) {
            if (count[g] == 0)
                continue;
            
            s += count[g];
            pref.push_back(s);
            vals.push_back(g);
        }

        vector<int> result;
        for (long long q: queries) {
            int pos = lower_bound(pref.begin(), pref.end(), q+1) - pref.begin();
            result.push_back(vals[pos]);
        }

        return result;
    }
};
