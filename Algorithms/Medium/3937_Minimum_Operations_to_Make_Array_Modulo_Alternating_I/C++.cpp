class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int n = nums.size();
        for (int i = 0; i < n; ++i)
            nums[i] %= k;
        
        vector<int> cost_odd(k), cost_even(k);
        for (int i = 0; i < n; ++i) {
            for (int target = 0; target < k; ++target) {
                int d = abs(nums[i]-target);
                int c = min(d, k-d);

                if (i%2 == 0)
                    cost_even[target] += c;
                else
                    cost_odd[target] += c;
            }
        }

        int result = INT_MAX;
        for (int x = 0; x < k; ++x) {
            for (int y = 0; y < k; ++y) {
                if (x == y)
                    continue;
                
                result = min(result, cost_even[x]+cost_odd[y]);
            }
        }

        return result;
    }
};
