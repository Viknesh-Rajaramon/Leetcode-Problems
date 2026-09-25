class Solution {
public:
    bool isPalindromic(string s) {
        int l = 0, r = s.length()-1;
        while (l <= r) {
            for (int bit = 7; bit >= 0; --bit) {
                int left = (s[l] >> bit) & 1, right = (s[r] >> (7 - bit)) & 1;
                if (left != right)
                    return false;
            }

            ++l;
            --r;
        }

        return true;
    }
};
