class Solution {
public:
    int climbStairs(int n, vector<int>& costs) {
        int result = 0, step_1 = 0, step_0 = 0;
        for (int cost : costs) {
            int temp = min({step_0+9, step_1+4, result+1});
            step_0 = step_1;
            step_1 = result;
            result = cost + temp;
        }
        
        return result;
    }
};
