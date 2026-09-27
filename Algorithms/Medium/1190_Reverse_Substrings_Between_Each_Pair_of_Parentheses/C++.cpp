class Solution {
public:
    string reverseParentheses(string s) {
        vector<string> result = {""};
        for (char c : s) {
            if (c == '(') {
                result.push_back("");
            } else if (c == ')') {
                string temp = result.back();
                result.pop_back();
                reverse(temp.begin(), temp.end());
                result.back() += temp;
            } else {
                result.back() += c;
            }
        }

        return result[0];
    }
};
