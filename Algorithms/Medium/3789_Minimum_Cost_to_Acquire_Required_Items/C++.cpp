class Solution {
public:
    long long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        long long cost_a = 1LL*need1*cost1 + 1LL*need2*cost2;
        long long cost_b = 1LL * min(need1, need2) * (costBoth - cost1 - cost2);
        long long cost_c = 1LL * max(need1, need2) * costBoth;
        return min(cost_a + min(0LL, cost_b), cost_c);
    }
};
