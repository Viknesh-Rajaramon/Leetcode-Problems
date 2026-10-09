class Solution {
public:
    int minInsertions(string s) {
        int result = 0, n = s.length(), left_count = 0, i = 0;
        while (i < n) {
            if (s[i] == '(') {
                ++left_count;
            } else {
                if (left_count > 0)
                    --left_count;
                else
                    ++result;
                
                if (i+1 < n && s[i+1] == ')')
                    ++i;
                else
                    ++result;
            }
            
            ++i;
        }

        result += 2*left_count;
        return result;
    }
};
