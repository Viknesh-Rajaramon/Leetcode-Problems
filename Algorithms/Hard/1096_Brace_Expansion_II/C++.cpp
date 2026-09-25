class Solution {
public:
    vector<string> braceExpansionII(string expression) {
        vector<char> op;
        vector<set<string>> stack;
        function<void()> ope = [&]() {
            int l = stack.size()-2, r = stack.size()-1;
            if (op.back() == '+') {
                stack[l].merge(stack[r]);
            } else {
                set<string> tmp;
                for (auto& left : stack[l]) {
                    for (auto& right : stack[r])
                        tmp.insert(left + right);
                }

                stack[l] = move(tmp);
            }

            op.pop_back();
            stack.pop_back();
        };

        for (int i = 0; i < expression.length(); ++i) {
            if (expression[i] == ',') {
                while(!op.empty() && op.back() == '*')
                    ope();

                op.push_back('+');
            } else if (expression[i] == '{') {
                if (i > 0 && (expression[i-1] == '}' || isalpha(expression[i-1])))
                    op.push_back('*');

                op.push_back('{');
            } else if (expression[i] == '}') {
                while(!op.empty() && op.back() != '{')
                    ope();

                op.pop_back();
            } else {
                if (i > 0 && (expression[i-1] == '}' || isalpha(expression[i-1])))
                    op.push_back('*');

                stack.push_back({string(1, expression[i])});
            }
        }

        while (!op.empty())
            ope();
        
        return {stack.back().begin(), stack.back().end()};
    }
};
