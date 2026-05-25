class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        int n = s.length();
        vector<bool> result(n, false);
        vector<int> pre(n, 0);
        for (int i = 0; i < minJump; ++i)
            pre[i] = 1;

        for (int i = minJump; i < n; ++i) {
            int left = i-maxJump;
            if (s[i] == '0') {
                int total = pre[i-minJump] - (left <= 0 ? 0 : pre[left-1]);
                result[i] = bool(total != 0);
            }

            pre[i] = pre[i-1] + int(result[i]);
        }

        return result[n-1];
    }
};
