class Solution {
public:
    vector<bool> validSubarrays(vector<int>& nums, int k, vector<vector<int>>& queries) {
        int block = (int)sqrt(nums.size()), ql = queries.size();
        vector<vector<int>> iqueries(ql, vector<int>(3));
        for (int i = 0; i < ql; i++) {
            iqueries[i][0] = queries[i][0];
            iqueries[i][1] = queries[i][1];
            iqueries[i][2] = i;
        }

        sort(iqueries.begin(), iqueries.end(), [&](const vector<int>& a, const vector<int>& b) {
                if (a[0] / block != b[0] / block) {
                    return a[0] / block < b[0] / block;
                }

                return a[1] < b[1];
            }
        );

        vector<bool> result(ql, false);
        int L = 0, R = -1, distinct = 0, odd = 0, maxElement = *max_element(nums.begin(), nums.end());
        vector<int> frequencies(maxElement + 1, 0);
        for (auto& iQ : iqueries) {
            int l = iQ[0], r = iQ[1], index = iQ[2];
            while (L > l) {
                --L;
                ++frequencies[nums[L]];
                if (frequencies[nums[L]] == 1)
                    ++distinct;

                if (frequencies[nums[L]] % 2 == 1)
                    ++odd;
                else
                    --odd;
            }

            while (R < r) {
                ++R;
                ++frequencies[nums[R]];
                if (frequencies[nums[R]] == 1)
                    ++distinct;

                if (frequencies[nums[R]] % 2 == 1)
                    ++odd;
                else
                    --odd;
            }

            while (L < l) {
                --frequencies[nums[L]];
                if (frequencies[nums[L]] == 0)
                    --distinct;

                if (frequencies[nums[L]] % 2 == 0)
                    --odd;
                else
                    ++odd;

                ++L;
            }

            while (r < R) {
                --frequencies[nums[R]];
                if (frequencies[nums[R]] % 2 == 1)
                    ++odd;
                else
                    --odd;

                if (frequencies[nums[R]] == 0)
                    --distinct;

                --R;
            }

            if (distinct == k && odd == 0) {
                result[index] = true;
            }
        }

        return result;
    }
};
