class Solution {
public:
    int minOperations(string s1, string s2) {
        int n = s1.length();
        if (n == 1) {
            if (s1 == "1" && s2 == "0")
                return -1;
            
            return (s1 != s2 ? 1 : 0);
        }

        int result = 0, l = 0;
        for (int i = 0; i < n; ++i) {
            if (s1[i] == '1' && s2[i] == '0') {
                ++l;
            } else {
                if (l > 0) {
                    result += (l/2) + (l%2)*2;
                    l = 0;
                }

                if (s1[i] == '0' && s2[i] == '1')
                    ++result;
            }
        }

        if (l > 0)
            result += (l/2) + (l%2)*2;

        return result;
    }
};
