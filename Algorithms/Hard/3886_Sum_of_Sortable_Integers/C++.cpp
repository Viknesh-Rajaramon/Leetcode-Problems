class Solution {
public:
    bool check_rotate_sorted(vector<int>& nums) {
        int n = nums.size(), downs = 0, down_val = 0, min_val = nums[0];
        for (int i = 0; i < n; i++) {
            min_val = min(min_val, nums[i]);
            if (nums[(i+1) % n] < nums[i]) {
                downs++;
                down_val = nums[(i+1) % n];
            }
        }

        if (downs == 0 || (downs == 1 && down_val == min_val))
            return true;

        return false;
    }

    vector<vector<int>> k_partition(vector<int>& nums, int k) {
        vector<vector<int>> res;
        int n = nums.size();
        for (int i = 0; i < n; i += k)
            res.emplace_back(nums.begin() + i, nums.begin() + i+k);

        return res;
    }

    int sortableIntegers(vector<int>& nums) {
        int result = 0, n = nums.size();
        for (int k = 1; k <= n; k++) {
            if (n % k != 0)
                continue;

            vector<vector<int>> partitions = k_partition(nums, k);
            int n_p = partitions.size();
            bool sortable = true;
            for (int i = 0; i < n_p; i++) {
                if (!check_rotate_sorted(partitions[i])) {
                    sortable = false;
                    break;
                }

                if (i + 1 < n_p && *max_element(partitions[i].begin(), partitions[i].end()) > *min_element(partitions[i + 1].begin(), partitions[i + 1].end())) {
                    sortable = false;
                    break;
                }
            }

            if (sortable)
                result += k;
        }

        return result;
    }
};
