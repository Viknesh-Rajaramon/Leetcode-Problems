class Solution {
public:
    int countRotations(string s, int k) {
        int result = s[0] == s.back() ? 1 : 0;
        for (int i = 0; i < s.length()-1; ++i)
            if (s[i] == s[i+1])
                ++result;

        if (k == result)
            return s.length() - result;

        return k == result-1 ? result : 0;
    }
};
