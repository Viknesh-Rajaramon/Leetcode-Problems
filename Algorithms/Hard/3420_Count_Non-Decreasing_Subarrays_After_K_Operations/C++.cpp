class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        long long result = 0, ops = 0;
        int n = nums.size(), l = 0;
        vector<int> stack;
        reverse(nums.begin(), nums.end());
        for (int r = 0; r < n; ++r) {
            while (!stack.empty() && nums[stack.back()] < nums[r]) {
                int j = stack.back();
                stack.pop_back();
                int i = !stack.empty() ? stack.back() : l-1;
                ops += 1LL * (nums[r] - nums[j]) * (j - i);
            }

            stack.push_back(r);
            while (ops > k) {
                ops -= max(0, nums[stack.front()] - nums[l]);
                if (stack.front() == l)
                    stack.erase(stack.begin());
                
                ++l;
            }

            result += r-l+1;
        }

        return result;
    }
};
