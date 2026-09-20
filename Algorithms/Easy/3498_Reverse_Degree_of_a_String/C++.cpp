class Solution {
public:
    int reverseDegree(string s) {
        int result = 0;
        for (int i = 0; i < s.length(); ++i)
            result += (i+1) * ('z' - s[i] + 1);
        
        return result;
    }
};
