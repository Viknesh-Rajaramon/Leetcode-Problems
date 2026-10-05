class Solution {
public:
    bool canTransform(vector<int>& source, vector<int>& target) {
        long long sum_ = 0;
        for (int i = 0; i < source.size(); ++i)
            sum_ += source[i] - target[i];
        
        return sum_ == 0;
    }
};
