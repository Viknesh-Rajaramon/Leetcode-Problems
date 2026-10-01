class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> bracket = {{'{', '}'}, {'(', ')'}, {'[', ']'}};
        vector<char> stack;
        for (char c : s) {
            if (bracket.count(c)) {
                stack.push_back(c);
            } else {
                if (stack.empty())
                    return false;

                char temp = stack.back();
                stack.pop_back();
                if (bracket[temp] != c)
                    return false;
            }
        }
        
        return stack.empty();
    }
};
