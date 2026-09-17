class Solution {
public:
    int largestInteger(int n, int s) {
        if (9*n < s)
            return -1;
        
        if (s == 0)
            return 0;
        
        int result = 0;
        for (int i = 0; i < n; ++i) {
            int d = min(s, 9);
            result = 10*result + d;
            s -= d;
        }
        
        return result;
    }
};
