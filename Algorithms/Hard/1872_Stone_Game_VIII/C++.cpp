class Solution {
public:
    int stoneGameVIII(vector<int>& stones) {
        int n = stones.size();
        for (int i = 1; i < n; ++i)
            stones[i] += stones[i-1];

        int result = stones[n-1];
        for (int i = n-2; i > 0; --i)
            result = max(result, stones[i] - result);

        return result;
    }
};
