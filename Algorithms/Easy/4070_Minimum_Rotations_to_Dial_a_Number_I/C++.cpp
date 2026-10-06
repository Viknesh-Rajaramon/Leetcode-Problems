class Solution {
public:
    int minRotations(string s) {
        int result = 0, curr = 0;
        for (char c : s) {
            int d = int(c-'0');
            result += min((d-curr+10) % 10, (curr-d+10) % 10);
            curr = d;
        }

        return result;
    }
};
