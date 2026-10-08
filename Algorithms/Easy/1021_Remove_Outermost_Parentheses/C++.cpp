class Solution {
public:
    string removeOuterParentheses(string s) {
        vector<string> temp;
        int left = 0, count = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '(') {
                ++count;
            } else {
                if (count == 1) {
                    temp.push_back(s.substr(left+1, i-left-1));
                    left = i+1;
                    count = 0;
                } else {
                    --count;
                }
            }
        }
        
        string result;
        for (string str : temp)
            result += str;
        
        return result;
    }
};
