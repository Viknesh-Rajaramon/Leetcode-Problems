class Solution {
public:
    int minimumGroups(vector<string>& words) {
        function<string(string)> duval = [&](string s) {
            int n = s.length();
            if (n <= 1)
                return s;

            int i = 0, j = 1, k = 0;
            while (i < n && j < n && k < n) {
                char cik = s[(i+k)%n], cjk = s[(j+k)%n];
                if (cik == cjk) {
                    ++k;
                } else if (cik < cjk) {
                    j += k + 1;
                    k = 0;
                } else {
                    i = max(i+k+1, j);
                    j = i+1;
                    k = 0;
                }
            }

            int ans = min(i, j) % n;
            return s.substr(ans) + s.substr(0, ans);
        };

        set<string> result;
        for (string w : words) {
            string even, odd;
            for (int i = 0; i < w.length(); i += 2) {
                even += w[i];
                if (i+1 < w.length())
                    odd += w[i+1];
            }

            result.insert(duval(even)+duval(odd));
        }

        return result.size();
    }
};
