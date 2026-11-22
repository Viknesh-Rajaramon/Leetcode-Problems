class Solution {
public:
    bool checkString(string s) {
        bool seen_b = false;
        for (char c : s) {
            if (c == 'a' && seen_b)
                return false;
            else if (c == 'b')
                seen_b = true;
        }

        return true;
    }
};
