class Solution {
public:
    int minOperations(string s) {
        int n = s.size();
        bool flag = true;
        for (int i = 0; i < n-1; ++i) {
            if (s[i] > s[i+1]) {
                flag = false;
                break;
            }
        }

        if (flag)
            return 0;

        if (n == 2)
            return -1;

        char min_c = *min_element(s.begin(), s.end()), max_c = *max_element(s.begin(), s.end());
        if (s[0] == min_c || s[n-1] == max_c)
            return 1;

        for (int i = 1; i < n-1; ++i)
            if (s[i] == max_c || s[i] == min_c)
                return 2;

        return 3;
    }
};
