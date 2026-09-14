class Solution {
public:
    string rearrangeString(string s, char x, char y) {
        vector<char> result;
        int count_x = 0, count_y = 0;
        for (char c : s) {
            if (c == x)
                ++count_x;
            else if (c == y)
                ++count_y;
            else
                result.push_back(c);
        }

        for (int i = 0; i < count_y; ++i)
            result.push_back(y);
        
        for (int i = 0; i < count_x; ++i)
            result.push_back(x);

        return string(result.begin(), result.end());
    }
};
