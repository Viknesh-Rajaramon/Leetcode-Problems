class Solution {
public:
    vector<int> result;
    void find(int low, int high, int n) {
        if (n > high)
            return;
        
        if (n >= low && n <= high)
            result.push_back(n);
        
        int s = n%10;
        if (s < 9)
            find(low, high, n*10 + s + 1);
    }

    vector<int> sequentialDigits(int low, int high) {
        for (int i = 1; i < 10; ++i)
            find(low, high, i);
        
        sort(result.begin(), result.end());
        return result;
    }
};
