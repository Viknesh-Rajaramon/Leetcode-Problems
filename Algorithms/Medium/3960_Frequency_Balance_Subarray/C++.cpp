class Solution {
public:
    int getLength(vector<int>& nums) {
        int result = 1, n = nums.size();
        for (int l = 0; l < n; ++l) {
            unordered_map<int, int> count;
            vector<int> freq(n+1);
            int min_ = n+1, max_ = 0, distinct = 0, occupied = 0;
            for (int r = l; r < n; ++r) {
                int old = count[nums[r]];
                int new_ = old+1;
                count[nums[r]] = new_;
                if (old == 0) {
                    ++distinct;
                    min_ = 1;
                } else {
                    --freq[old];
                    if (freq[old] == 0)
                        --occupied;
                }

                if (freq[new_] == 0)
                    ++occupied;

                ++freq[new_];
                max_ = max(max_, new_);

                if (old > 0 && old == min_ && freq[old] == 0)
                    while (freq[min_] == 0)
                        ++min_;

                if (distinct == 1 || (occupied == 2 && max_ == 2*min_))
                    result = max(result, r-l+1);
            }
        }

        return result;
    }
};
