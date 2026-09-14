class Solution {
public:
    int minCost(string source, string target, vector<vector<string>>& rules, vector<int>& costs) {
        int n = source.length();
        vector<int> dp(n+1, -1);
        function<int(int)> f = [&](int i) {
            if (i == n)
                return 0;
            
            if (dp[i] != -1)
                return dp[i];
            
            int result = INT_MAX;
            if (source[i] == target[i])
                result = f(i+1);
            
            for (int j = 0; j < rules.size(); ++j) {
                string x = rules[j][0], y = rules[j][1];
                if (i + x.length() > n)
                    continue;
                
                bool valid = true;
                int wildcard = 0;
                for (int k = 0; k < x.length(); ++k) {
                    if (x[k] != '*' && source[i+k] != x[k]) {
                        valid = false;
                        break;
                    }
                    
                    if (x[k] == '*')
                        ++wildcard;
                    
                    if (y[k] != target[i+k]) {
                        valid = false;
                        break;
                    }
                }

                if (!valid)
                    continue;
                
                int nxt = f(i + x.length());
                if (nxt != INT_MAX)
                    result = min(result, costs[j] + wildcard + nxt);
            }

            dp[i] = result;
            return result;
        };
        
        int result = f(0);
        return result != INT_MAX ? result : -1;
    }
};
