class Solution {
public:
    int passwordStrength(string password) {
        int result = 0;
        unordered_set<char> chars;
        for (char c : password)
            chars.insert(c);
        
        for (char c : chars) {
            if (97 <= c && c <= 122)
                result += 1;
            else if (65 <= c && c <= 90)
                result += 2;
            else if (48 <= c && c <= 57)
                result += 3;
            else
                result += 5;
        }

        return result;
    }
};
