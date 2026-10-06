class Solution {
public:
    int minAddToMakeValid(string s) {
        int result = 0, open_count = 0;
        for (char c : s) {
            if (c == '(') {
                ++open_count;
            } else {
                if (open_count > 0)
                    --open_count;
                else
                    ++result;
            }
        }
        
        return result + open_count;
    }
};
