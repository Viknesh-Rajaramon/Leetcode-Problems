class Solution {
public:
    string evaluate(string s, vector<vector<string>>& knowledge) {
        string result;
        unordered_map<string, string> d;
        int start = -1;
        for (auto& kd : knowledge)
            d[kd[0]] = kd[1];

        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '(') {
                start = i;
            } else if (s[i] == ')') {
                if (d.count(s.substr(start+1, i-start-1)))
                    result += d[s.substr(start+1, i-start-1)];
                else
                    result.push_back('?');
                
                start = -1;
            } else if (start < 0) {
                result.push_back(s[i]);
            }
        }

        return result;
    }
};
