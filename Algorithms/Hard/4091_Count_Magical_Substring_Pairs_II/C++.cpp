class Solution {
public:
    long long countMagicalPairs(string s) {
        int n = s.length();
        vector<vector<int>> l(n, vector<int>(27)), r(n, vector<int>(27));
        vector<int> pos(26, -1);
        for (int i = 0; i < n; ++i) {
            pos[int(s[i]-97)] = i;
            vector<int> p;
            for (int x : pos)
                if (x != -1)
                    p.push_back(x);

            sort(p.rbegin(), p.rend());
            for (int k = 0; k < p.size(); ++k)
                l[i][k+1] = p[k] - ((k+1 < p.size()) ? p[k+1] : -1);
        }

        fill(pos.begin(), pos.end(), n);
        for (int i = n-1; i >= 0; --i) {
            pos[int(s[i]-97)] = i;
            vector<int> q;
            for (int x : pos)
                if (x != n)
                    q.push_back(x);

            sort(q.begin(), q.end());
            for (int k = 0; k < q.size(); ++k)
                r[i][k+1] = ((k+1 < q.size()) ? q[k+1] : n) - q[k];
        }
        
        long long result = 0;
        for (int i = 0; i < n-1; ++i) {
            for (int k = 1; k <= 26; ++k)
                result += 1LL * l[i][k] * r[i+1][k];
        }

        return result;
    }
};
