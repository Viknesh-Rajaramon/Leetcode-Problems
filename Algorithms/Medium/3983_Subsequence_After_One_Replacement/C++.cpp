class Solution {
public:
    bool canMakeSubsequence(string s, string t) {
        int m = s.length(), n = t.length();
        if (m > n)
            return false;

        bool replaced = false;
        char rch;
        int i = 0, j = 0;
        while (i < m && j < n) {
            if (s[i] == t[j]) {
                ++i;
            } else {
                if (!replaced) {
                    replaced = true;
                    rch = s[i++];
                } else {
                    if (rch == t[j])
                        replaced = false;
                }
            }
                    
            ++j;
        }
        
        return (i == m);
    }
};
