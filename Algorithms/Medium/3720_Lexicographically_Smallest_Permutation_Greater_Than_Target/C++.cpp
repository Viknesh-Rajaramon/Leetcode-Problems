class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n = s.length();
        vector<int> freq(26);
        for (char c : s)
            ++freq[c-'a'];
        
        string result = "", temp = "";
        auto dfs = [&](auto& self, int pos, bool found) -> bool {
            if (pos == n) {
                if (temp > target) {
                    result = temp;
                    return true;
                }

                return false;
            }

            int start = found ? 0 : target[pos] - 'a';
            for (int i = start; i < 26; ++i) {
                if (freq[i] > 0) {
                    --freq[i];
                    temp.push_back('a' + i);
                    if (self(self, pos+1, found || i > target[pos] - 'a'))
                        return true;
                    
                    temp.pop_back();
                    ++freq[i];
                }
            }

            return false;
        };

        dfs(dfs, 0, false);
        return result;
    }
};
