class Solution {
public:
    int maximumSaleItems(vector<vector<int>>& items, int budget) {
        int n = items.size(), mn = INT_MAX;
        vector<long long> cnt(n+1), mul(n+1);
        for (int i = 0; i < n; ++i) {
            mn = min(mn, items[i][1]);
            cnt[items[i][0]]++;
        }

        for (int f=1; f <= n; ++f)
            for (int m = f; m <= n; m += f)
                mul[f] += cnt[m];
        
        map<int, long long> mp;
        for (int i = 0; i < n; ++i) {
            int d = mul[items[i][0]]-1;
            if (d > 0 && items[i][1] <= 2*mn)
                mp[items[i][1]] += d;
        }

        int result = 0;
        for (auto &it : mp) {
            int x = it.first, y = it.second;
            long long pk = min(y, budget/x);
            budget -= pk*x;
            result += 2*pk;
        }

        result += budget/mn;
        return result;
    }
};
