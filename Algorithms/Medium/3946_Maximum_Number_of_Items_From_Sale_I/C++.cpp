class Solution {
public:
    int maximumSaleItems(vector<vector<int>>& items, int budget) {
        int n = items.size();
        vector<vector<int>> pre(n);
        for (int i = 0; i < n; ++i) {
            int c = 1;
            for (int j = 0; j < n; ++j) {
                if (i == j)
                    continue;
                
                if (items[j][0] % items[i][0] == 0)
                    ++c;
            }
            
            vector<int> temp(items[i]);
            temp.push_back(c);
            pre[i] = temp;
        }

        vector<int> dp(budget+1);
        for (int i = 0; i < n; ++i) {
            int p = pre[i][1], cnt = pre[i][2];
            for (int b = p; b <= budget; ++b)
                dp[b] = max(dp[b], dp[b-p]+1);
            
            for (int b = budget; b >= p; --b)
                dp[b] = max(dp[b], dp[b-p]+cnt);
        }

        int result = 0;
        for (int val : dp)
            if (val > result)
                result = val;

        return result;
    }
};
