class Solution {
public:
    bool threeFibonacciSum(int n) {
        int f_0 = 0, f_1 = 1, f_2 = 1;
        while (f_0 + f_1 + f_2 <= n) {
            if (f_0 + f_1 + f_2 == n)
                return true;
            
            f_0 = f_1;
            f_2 += f_1;
            f_1 = f_2 - f_1;
        }
        
        return false;
    }
};
