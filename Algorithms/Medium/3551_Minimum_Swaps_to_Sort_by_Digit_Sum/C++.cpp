class Solution {
public:
    int minSwaps(vector<int>& nums) {
        function<int(int)> sum_of_digits = [&](int num) {
            int result = 0;
            while (num > 0) {
                result += num % 10;
                num /= 10;
            }
            
            return result;
        };

        int result = 0, n = nums.size();
        vector<int> sorted_nums = nums;
        sort(sorted_nums.begin(), sorted_nums.end(), [&](int a, int b) {
            int p = sum_of_digits(a), q = sum_of_digits(b);
            return (p != q) ? (p < q) : (a < b);
        });

        unordered_map<int, int> val_idx_map;
        for (int i = 0; i < n; ++i)
            val_idx_map[sorted_nums[i]] = i;
        
        vector<bool> visited(n);
        for (int i = 0; i < n; ++i) {
            if (visited[i] || val_idx_map[nums[i]] == i)
                continue;

            int cycle_size = 0, j = i;
            while (!visited[j]) {
                visited[j] = true;
                j = val_idx_map[nums[j]];
                ++cycle_size;
            }

            if (cycle_size > 1)
                result += cycle_size - 1;
        }

        return result;
    }
};
