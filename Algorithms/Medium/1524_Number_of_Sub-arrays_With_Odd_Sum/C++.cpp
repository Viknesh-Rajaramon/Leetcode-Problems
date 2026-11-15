class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        int n = arr.size(), odd_count = 0, curr_sum = 0;
        for (int num : arr) {
            curr_sum += num;
            if (curr_sum % 2 == 1)
                ++odd_count;
        }
        
        return (1LL * odd_count * (n - odd_count + 1)) % ((int)1e9+7);
    }
};
