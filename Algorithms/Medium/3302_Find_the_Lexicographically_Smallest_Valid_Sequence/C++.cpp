class Solution {
public:
    vector<int> validSequence(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        vector<int> last(n);
        int j = n-1;
        for (int i = m-1; i >= 0; --i) {
            if (word1[i] == word2[j]) {
                last[j] = i;
                if (--j < 0)
                    break;
            }
        }

        vector<int> result;
        bool skip = false;
        j = 0;
        for (int i = 0; i < m; ++i) {
            if (j == n)
                break;
            
            if (word1[i] == word2[j]) {
                result.push_back(i);
                ++j;
            } else {
                if (!skip && (j == n-1 || last[j+1] > i)) {
                    skip = true;
                    result.push_back(i);
                    ++j;
                }
            }
        }

        if (j != n)
            return vector<int>();

        return result;
    }
};
