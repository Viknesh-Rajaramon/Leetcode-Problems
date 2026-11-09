class Solution {
public:
    long long countValidSubstrings(string s) {
        long long result = 0;
        int a = -1, ab = -1, abc = -1;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == 'a')
                a = i;
            else if (s[i] == 'b' && a != -1)
                ab = a;
            else if (s[i] == 'c' && ab != -1)
                abc = ab;
            
            result += i - abc;
        }

        return result;
    }
};
