class Solution {
public:
    int distinctSubseqII(string s) {
        int dp = 1;
        vector<int> last(26);
        const int mod = 1e9+7;
        for (char c : s) {
            int new_dp = ((dp*2%mod) - last[c-'a'] + mod) % mod;
            last[c-'a'] = dp;
            dp = new_dp;
        }

	    return (dp - 1 + mod) % mod;
    }
};
