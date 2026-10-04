class Solution {
public:
    bool checkValidString(string s) {
        int open_count = 0, closed_count = 0, n = s.length()-1;
        for (int i = 0; i <= n; ++i) {
            if (s[i] == '(' || s[i] == '*')
                ++open_count;
            else
                --open_count;
            
            if (s[n-i] == ')' || s[n-i] == '*')
                ++closed_count;
            else
                --closed_count;
            
            if (open_count < 0 || closed_count < 0)
                return false;
        }

        return true;
    }
};
