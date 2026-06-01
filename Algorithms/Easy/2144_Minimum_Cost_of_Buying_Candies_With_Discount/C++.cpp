class Solution {
public:
    int minimumCost(vector<int>& cost) {
        sort(cost.begin(), cost.end(), greater<int>());
        int result = 0, n = cost.size();
        for (int i = 0; i < n; i += 3)
            result += cost[i] + (i+1 < n ? cost[i+1] : 0);

        return result;
    }
};
