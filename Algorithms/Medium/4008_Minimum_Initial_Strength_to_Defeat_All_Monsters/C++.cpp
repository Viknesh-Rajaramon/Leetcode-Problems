class Solution {
public:
    long long minInitialStrength(vector<int>& monsters, vector<vector<int>>& boosts) {
        int n = monsters.size();
        vector<long long> diff(n+1), bonus(n);
        for (auto& boost : boosts) {
            diff[boost[0]] += boost[2];
            diff[boost[1]+1] -= boost[2];
        }
        
        bonus[0] = diff[0];
        for (int i = 1; i < n; ++i)
            bonus[i] = bonus[i-1] + diff[i];
        
        long long result = 0;
        for (int i = n-1; i >= 0; --i) {
            if (result == 0)
                result = (monsters[i] <= bonus[i]) ? 0 : (monsters[i] - bonus[i]);
            else
                result += monsters[i];
        }

        return result;
    }
};
