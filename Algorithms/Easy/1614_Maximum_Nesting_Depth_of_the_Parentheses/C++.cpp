class Solution {
public:
    int maxDepth(string s) {
        int result = 0, curr = 0;
        for (char c : s) {
            if (c == '(') {
                ++curr;
                result = max(result, curr);
            } else if (c == ')') {
                --curr;
            }
        }
            
        return result;
    }
};
