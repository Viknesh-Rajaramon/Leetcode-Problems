class Solution {
public:
    int longestSubarray(vector<int>& nums, int k) {
        int n = nums.size(), prefix = 0;
        vector<int> first(k, n+1), last(k, -1);
        vector<vector<int>> pos(k);
        first[0] = 0;
        last[0] = 0;
        for (int i = 0; i < n; ++i) {
            int val = ((nums[i] % k) + k) % k;
            pos[val].push_back(i);
            prefix = (prefix + val) % k;
            last[prefix] = i+1;
            if (first[prefix] == n+1)
                first[prefix] = i+1;
        }
        
        int result = 0;
        for (int i = 0; i < k; ++i)
            if (first[i] != n+1)
                result = max(result, last[i] - first[i]);
        
        for (int i = 0; i < k; ++i) {
            if (pos[i].empty())
                continue;
            
            int target = (2*i) % k;
            for (int j = 0; j < k; ++j) {
                if (first[j] == n+1)
                    continue;
                
                int r = (j+target)%k;
                if (last[r] == -1 || last[r] - first[j] <= result)
                    continue;
                
                int idx = lower_bound(pos[i].begin(), pos[i].end(), first[j]) - pos[i].begin();
                if (idx < pos[i].size() && pos[i][idx] < last[r])
                    result = last[r] - first[j];
            }
        }

        return result;
    }
};
