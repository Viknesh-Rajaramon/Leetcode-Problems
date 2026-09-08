class Solution {
public:
    long long maxSum(vector<int>& nums, int k) {
        int n = nums.size();
        long long result = LLONG_MIN;
        vector<int> sorted = nums;
        sort(sorted.begin(), sorted.end());

        multiset<int> candidates, others, initial_candidates, initial_others;
        for (int i = 0; i < max(0, n-k); ++i)
            initial_others.insert(sorted[i]);
          

        for (int i = max(0, n-k); i < n; ++i)
            initial_candidates.insert(sorted[i]);

        for (int start = 0; start < n; ++start) {
            candidates = initial_candidates;
            others = initial_others;
            long long currentSum = 0;

            for (int end = start; end < n; ++end) {
                if(!others.empty()) {
                    int val;
                    auto it_other = others.find(nums[end]);
                    if(it_other != others.end()) {
                        val = nums[end];
                        others.erase(it_other);
                    } else {
                        auto it_largest_other = prev(others.end());
                        val = *it_largest_other;
                        others.erase(it_largest_other);
                    }

                    candidates.insert(val);
                }

                auto it_largest_candidate = prev(candidates.end());
                currentSum += *it_largest_candidate;
                candidates.erase(it_largest_candidate);

                result = max(result, currentSum);
            }
        }

        return result;
    }
};
