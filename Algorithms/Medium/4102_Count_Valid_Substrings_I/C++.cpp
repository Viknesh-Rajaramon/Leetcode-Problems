class Solution {
public:
    long long countValidSubstrings(string s) {
        long long result = 0;
        int l = 0;
        for (int r = 0; r < s.length(); ++r) {
            if (r >= 2 && s[r-2] == 'a' && s[r-1] == 'b' && s[r] == 'c')
                l = r-1;
            
            result += r-l+1;
        }

        return result;
    }
};
