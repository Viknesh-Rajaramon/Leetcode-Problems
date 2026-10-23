class Solution {
public:
    int sortPermutation(vector<int>& nums) {
        int result = 0;
        bool flag = false;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == i)
                continue;

            if (!flag) {
                result = nums[i];
                flag = true;
            } else {
                result &= nums[i];
            }
        }
        
        return flag ? result : 0;
    }
};
