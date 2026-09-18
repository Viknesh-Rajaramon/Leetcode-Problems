class Solution {
public:
    int countValidPrefixes(string s) {
        int result = 0, ones = 0, zeros = 0;
        for (char c : s) {
            if (c == '1')
                ++ones;
            else
                ++zeros;
            
            if (abs(zeros - ones) < 2)
                ++result;
        }

        return result;
    }
};
