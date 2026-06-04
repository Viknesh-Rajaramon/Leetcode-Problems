class Solution {
public:
    int totalWaviness(int num1, int num2) {
        int result = 0;
        for (int num = num1; num <= num2; ++num) {
            string s = to_string(num);
            for (int j = 1; j < s.length()-1; ++j)
                if ((s[j-1] > s[j] && s[j] < s[j+1]) || (s[j-1] < s[j] && s[j] > s[j+1]))
                    ++result;
        }

        return result;
    }
};
