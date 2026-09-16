class Solution {
public:
    vector<bool> transformStr(string s, vector<string>& strs) {
        int total_0 = count(s.begin(), s.end(), '0');
        function<bool(string)> check = [&](string t) {
            int count_0 = count(t.begin(), t.end(), '0'), count_q = count(t.begin(), t.end(), '?');
            if (total_0 < count_0 || total_0 > count_0 + count_q)
                return false;

            vector<char> x(t.begin(), t.end());
            for (int i = 0; i < x.size(); ++i) {
                if (count_0 == total_0)
                    break;

                if (x[i] == '?') {
                    x[i] = '0';
                    ++count_0;
                }
            }

            int i = 0, j = 0;
            for (int k = 0; k < total_0; ++k) {
                while (s[i] != '0')
                    ++i;

                while (x[j] != '0')
                    ++j;

                if (i < j)
                    return false;

                ++i;
                ++j;
            }

            return true;
        };

        vector<bool> result;
        for (string t : strs)
            result.push_back(check(t));

        return result;
    }
};
