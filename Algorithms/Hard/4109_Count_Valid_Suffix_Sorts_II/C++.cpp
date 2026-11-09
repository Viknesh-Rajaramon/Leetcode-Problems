class Solution {
public:
    vector<int> countSuffix(vector<int>& nums, vector<int>& target) {
        int n = nums.size(), m = target.size();
        vector<int> result(m-n+1), com = nums;
        com.push_back(0);
        com.insert(com.end(), target.begin(), target.end());
        int L_com = com.size();
        vector<int> z(L_com);
        int l = 0, r = 0;
        for (int i = 1; i < L_com; ++i) {
            if (i <= r)
                z[i] = min(r-i+1, z[i-l]);
            
            while (i + z[i] < L_com && com[z[i]] == com[i + z[i]])
                ++z[i];
            
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }
                
        vector<int> pre(m);
        for (int i = 1; i < m; ++i)
            pre[i] = target[i-1] >= target[i] ? pre[i-1] : i;
            
        vector<int> freq(100001);
        int bad = 0;
        for (int x : nums) {
            if (freq[x] == 1)
                --bad;
            
            --freq[x];
        }

        for (int i = 0; i < n; ++i) {
            if (freq[target[i]] == 0)
                ++bad;
            
            ++freq[target[i]];
        }
            
        int zs = n+1;
        for (int k = 0; k < m-n+1; ++k) {
            if (bad == 0) {
                int min_I = max(0, pre[k+n-1] - k);
                int max_I = min(n-1, z[zs + k]);
                if (max_I >= min_I)
                    result[k] = max_I - min_I + 1;
            }
                    
            if (k+n < m) {
                if (freq[target[k]] == 1)
                    --bad;
                
                --freq[target[k]];
                if (freq[target[k+n]] == 0)
                    ++bad;
                
                ++freq[target[k+n]];
            }
        }
                
        return result;
    }
};
