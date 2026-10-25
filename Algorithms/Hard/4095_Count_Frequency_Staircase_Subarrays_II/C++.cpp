class Solution {
public:
    int countStaircase(vector<int>& nums) {
        int n = nums.size();
        vector<int> ind(n);
        unordered_map<int, vector<int>> pos;
        for (int i = 0; i < n; ++i) {
            ind[i] = pos[nums[i]].size();
            pos[nums[i]].push_back(i);
        }

        int result = 0;
        for (int i = 0; i < n; ++i) {
            unordered_set<int> seen;
            int l = i, r = n-1;
            for (int j = i; j < n; ++j) {
                if (j > r)
                    break;

                if (seen.contains(nums[j]))
                    continue;

                seen.insert(nums[j]);
                int k = seen.size();
                if (ind[j]+k-1 >= pos[nums[j]].size())
                    break;

                l = max(l, pos[nums[j]][ind[j] + k - 1]);
                r = min(r, (ind[j] + k < pos[nums[j]].size()) ? pos[nums[j]][ind[j] + k] : n-1);
                if (l > r)
                    break;

                int tmp = i + k*(k + 1)/2 - 1;
                if (l <= tmp && tmp <= r)
                    ++result;
            }
        }
            
        return result;
    }
};
