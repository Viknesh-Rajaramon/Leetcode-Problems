class Solution {
public:
    string digitSum(string s, int k) {
        while (s.length() > k) {
            int n = s.length();
            string tmp;
            for (int i = 0; i < n; i += k) {
                int val = 0;
                for (int j = i; j < min(i+k, n); ++j)
                    val += s[j] - '0';
                
                tmp.append(to_string(val));
            }

            s = tmp;
        }

        return s;
    }
};
