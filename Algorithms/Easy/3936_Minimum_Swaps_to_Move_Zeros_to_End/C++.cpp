class Solution {
public:
    int minimumSwaps(vector<int>& nums) {
        int result = 0, left = 0, right = nums.size()-1;
        while (left < right) {
            while (right >= 0 && nums[right] == 0)
                right -= 1;
            
            if (right < 0 || right < left)
                break;

            if (nums[left] == 0) {
                result += 1;
                right -= 1;
            }

            left += 1;
        }

        return result;
    }
};
