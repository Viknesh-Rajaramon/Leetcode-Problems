class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        int max_1 = INT_MIN, max_2 = INT_MIN, max_3 = INT_MIN;
        int min_1 = INT_MAX, min_2 = INT_MAX;
        for (int num: nums) {
            if (num > max_1) {
			    max_3 = max_2;
                max_2 = max_1;
                max_1 = num;
		    } else if (num > max_2) {
                max_3 = max_2;
                max_2 = num;
            } else if (num > max_3)
                max_3 = num;

            if (num < min_1) {
                min_2 = min_1;
                min_1 = num;
            } else if (num < min_2)
                min_2 = num;
        }

        return max(max_1*max_2*max_3, min_1*min_2*max_1);
    }
};
