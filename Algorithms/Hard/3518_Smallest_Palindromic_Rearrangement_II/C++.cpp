class Solution {
public:
    string smallestPalindrome(string s, int k) {
        int n = s.size();
        vector<int> count(26);
        for (int i = 0; i < n/2; ++i)
            ++count[s[i] - 'a'];

        int total = 0, counting = 1, remain = 0, i = 0;
        for (i = 25; i >= 0; --i) {
            for (int c = 1; c <= count[i]; ++c) {
                ++total;
                counting = counting * total / c;
                if (counting >= k) {
                    remain = count[i] - c;
                    break;
                }
            }

            if (counting >= k)
                break;
        }

        if (counting < k)
            return "";

        string result(n, 0);
        int l = 0;
        for (int j = 0; j <= i; ++j) {
            const char x = 'a' + j;
            const int c = j != i ? count[j] : remain;
            
            for (int _ = 0; _ < c; ++_) {
                --count[j];
                result[l++] = x;
            }
        }

        while (total) {
            for (int j = i; j < 26; ++j) {
                if (!count[j])
                    continue;

                const auto new_count = static_cast<int64_t>(counting) * count[j] / total;
                if (new_count < k) {
                    k -= new_count;
                    continue;
                }

                counting = new_count;
                --count[j];
                --total;
                result[l++] = 'a' + j;
                break;
            }
        }

        if (n & 1)
            result[l++] = s[n/2];

        for (int i = l-1-n%2; i >= 0; --i)
            result[l++] = result[i];

        return result;
    }
};
