class Solution {
public:
    int countValidSubsets(vector<int>& parent, vector<int>& nums, int k) {
        const long long int mod = 1e9+7;
        int n = parent.size();
        vector<vector<long long int>> dp0(n, vector<long long int>(k, 0));
        vector<vector<long long int>> dp1(n, vector<long long int>(k, 0));
        for (int i = 0; i < n; ++i) {
            dp0[i][0] = 1;
            dp1[i][nums[i]%k] = 1;
        }

        for (int i = n-1; i > 0; --i) {
            vector<long long int> p_nz_0, p_nz_1, child_ways_any(k), c_nz_any, c_nz_0;
            for (int r = 0; r < k; ++r) {
                if (dp0[parent[i]][r] > 0)
                    p_nz_0.push_back(r);
                
                if (dp1[parent[i]][r] > 0)
                    p_nz_1.push_back(r);
                
                child_ways_any[r] = (dp0[i][r] + dp1[i][r]) % mod;
                if (child_ways_any[r] > 0)
                    c_nz_any.push_back(r);
                
                if (dp0[i][r] > 0)
                    c_nz_0.push_back(r);
            }

            vector<long long int> new_dp0(k), new_dp1(k);
            for (int r1 : p_nz_0) {
                for (int r2 : c_nz_any) {
                    int idx = (r1+r2) % k;
                    new_dp0[idx] = (new_dp0[idx] + dp0[parent[i]][r1]*child_ways_any[r2])%mod;
                }
            }

            for (int r1 : p_nz_1) {
                for (int r2 : c_nz_0) {
                    int idx = (r1+r2) % k;
                    new_dp1[idx] = (new_dp1[idx] + dp1[parent[i]][r1]*dp0[i][r2])%mod;
                }
            }

            dp0[parent[i]] = new_dp0;
            dp1[parent[i]] = new_dp1;
        }

        return (dp0[0][0] + dp1[0][0] - 1) % mod;
    }
};
