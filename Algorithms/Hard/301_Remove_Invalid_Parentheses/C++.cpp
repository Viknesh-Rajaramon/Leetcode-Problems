class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        function<string(string)> reverse = [&](string s) {
            string rev_str = "";
            for (int i = s.length()-1; i >= 0; --i)
                rev_str += s[i];
            
            return rev_str;
        };
    
        vector<string> result;
        function<void(string, int, int, char, char)> helper = [&](string s, int left, int right, char open_p, char close_p) {
            int count = 0;
            while (right < s.length()) {
                if (s[right] == open_p)
                    ++count;
                else if (s[right] == close_p)
                    --count;

                if (count < 0)
                    break;

                ++right;
            }

            if (count < 0) {
                while (left <= right) {
                    if ((s[left] == close_p) && (left == 0 || s[left] != s[left-1]))
                        helper(s.substr(0, left) + s.substr(left+1, s.length()-left-1), left, right, open_p, close_p);
                    
                    ++left;
                }
            } else if (count > 0) {
                helper(reverse(s), 0, 0, close_p, open_p);
            } else {
                if (open_p == '(')
                    result.push_back(s);
                else
                    result.push_back(reverse(s));
            }
        };

        helper(s, 0, 0, '(', ')');
        return result;
    }
};
