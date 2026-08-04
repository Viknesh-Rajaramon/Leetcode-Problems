class Solution {
public:
    vector<int> findMissingElements(vector<int>& nums) {
        vector<int> result;
        set<int> s(nums.begin(), nums.end());
        int min_ = *min_element(nums.begin(), nums.end());
        int max_ = *max_element(nums.begin(), nums.end());
        for (int num = min_; num <= max_; ++num)
            if (s.find(num) == s.end())
                result.push_back(num);

        return result;
    }
};
