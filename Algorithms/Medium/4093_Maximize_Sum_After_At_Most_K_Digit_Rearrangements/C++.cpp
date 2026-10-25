class Solution {
public:
    long long maximizeSum(vector<int>& nums, int k) {
        long long result = 0;
        vector<int> gains;
        for (int num : nums) {
            result += num;
            vector<int> freq(10);
            int x = num;
            while (x > 0) {
                ++freq[x%10];
                x /= 10;
            }
            
            int max_num = 0;
            for (int d = 9; d >= 0; --d) {
                for (int j = 0; j < freq[d]; ++j)
                    max_num = max_num*10 + d;
            }
            
            if (max_num > num)
                gains.push_back(max_num - num);
        }

        sort(gains.rbegin(), gains.rend());
        for (int i = 0; i < min(k, (int)gains.size()); ++i)
            result += gains[i];
        
        return result;
    }
};
