class Solution {
public:
    int minimumPushes(string word) {
        int n = word.size();
        int m = (n-1)/8 + 1;
        return m * (n - 4*(m-1));
    }
};
