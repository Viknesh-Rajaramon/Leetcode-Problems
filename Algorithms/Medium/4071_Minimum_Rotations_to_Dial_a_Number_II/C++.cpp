class Solution {
public:
    int minRotations(int n, string s) {
        function<int(int, int)> dist = [&](int a, int b) {
            int d = abs(a-b);
            return min(d, 10-d);
        };

        int base = dist(0, int(s[0]-'0'));
        for (int i = 0; i < n-1; ++i)
            base += dist(int(s[i]-'0'), int(s[i+1]-'0'));

        int result = min(base, base-dist(0, int(s[0]-'0'))+dist(0, int(s[n-1]-'0')));
        for (int k = 0; k < n-1; ++k)
            result = min(result, base-dist(int(s[k]-'0'), int(s[k+1]-'0'))+dist(int(s[k]-'0'), int(s[n-1]-'0')));

        return result;
    }
};
