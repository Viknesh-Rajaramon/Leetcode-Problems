class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        int n = nums.size();
        vector<long long> squares(n);
        for (int i = 0; i < n; ++i)
            squares[i] = nums[i]*nums[i];
        
        sort(squares.rbegin(), squares.rend());
        long long result = 0;
        int k = (n+1)/2;
        for (int i = 0; i < n; ++i)
            result += (i < k) ? squares[i] : -squares[i];
        
        return result;
    }
};
