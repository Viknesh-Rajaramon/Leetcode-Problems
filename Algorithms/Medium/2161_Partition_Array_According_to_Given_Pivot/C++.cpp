class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector <int>less, equal, more;
        for (int num: nums) {
            if (num < pivot)
                less.push_back(num);
            else if (num > pivot)
                more.push_back(num);
            else
                equal.push_back(num);
        }

        less.insert(less.end(), equal.begin(), equal.end());
        less.insert(less.end(), more.begin(), more.end());

        return less;
    }
};
