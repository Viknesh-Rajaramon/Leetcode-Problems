class Solution {
public:
    string lexPalindromicPermutation(string s, string target) {
        map<char, int> freq;
        for (char c : s)
            ++freq[c];
        
        int odd_count = 0;
        for (auto &[c, count] : freq)
            if (count%2)
                ++odd_count;

        if (odd_count > 1)
            return "";
        
        int n = s.length();
        string sorted_chars;
        for (auto &[c, count] : freq)
            sorted_chars += c;
        
        string odd = "";
        if (n%2) {
            for (char c : sorted_chars) {
                if (freq[c]%2) {
                    odd = c;
                    break;
                }
            }
        }

        for (auto &[c, count] : freq)
            count /= 2;
        
        string result = "", path = "";
        function<void(int, bool)> dfs = [&](int i, bool tight) {
            if (!result.empty())
                return;
            
            if (i == n/2) {
                string candidate = path + odd + string(path.rbegin(), path.rend());
                if (!tight || candidate > target)
                    result = candidate;
                
                return;
            }

            char low = '\0';
            if (tight)
                low = target[i];
            
            for (char c : sorted_chars) {
                if ((!tight || c >= low) && freq[c] > 0) {
                    path += c;
                    --freq[c];
                    dfs(i+1, tight && c == low);
                    path.pop_back();
                    ++freq[c];
                    if (!result.empty())
                        break;
                }
            }
        };

        dfs(0, true);
        return result;
    }
};
